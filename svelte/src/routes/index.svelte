<script lang="ts">
	import BgHero from './BgHero.svelte';
	import Hero3d from './Hero3d.svelte';

	import TwitterLink from './components/home/TwitterLink.svelte';
	import {subContractAbi} from '$lib/abi'
	import Items from '$lib/Items.svelte'
	import Bet from '$lib/Bet.svelte';

	export let trad = {};
	export let sections = {};

	const subContractAddress = '0x81663d5149cADBbc48CF1a7F21b05719Ee1420A9';

	let provider;
	let amount = trad.connect;
	let account;
	let hasFinied = false;

	const connect = async () => {
		const accounts = await window.ethereum
			.request({
				method: 'eth_requestAccounts'
			})
			.catch((err) => {
				console.log(err.code);
			});

		account = accounts[0];
		let subContract = new ethers.Contract(subContractAddress, subContractAbi, provider);
		let bal = await subContract.balanceOf(account);
		amount = bal.toString() / Math.pow(10, 9);
		amount = `${amount.toFixed(2)}`;
	};
	const peko = `@${trad.peko}`;
	const finance = `@${trad.finance}`;
	let fullHight = '';
	$: if (hasFinied) {
		fullHight = 'h-screen';
	}
</script>

<section class="text-slate-300 {fullHight}">
	<div>
		<div class="opacity-20">
			<!-- <BgHero /> -->
		</div>
		<div class="p-5 ">
			<button
				class=" bg-orange-500 float-right px-8 rounded-full border-2 border-orange-600 text-slate-100 "
				on:click={connect}
			>
				{#if amount !== trad.connect}
					<span class="font-thin italic">{amount} </span>
					<span class="font-bold italic">$NFTL </span>
				{:else}
					<span class="font-base italic">{amount} </span>
				{/if}
			</button>
			<!-- {$chainId} -->
			<!-- {JSON.stringify($chainData)} -->
			<div>
				<img src="NFTL.webp" alt="logo" class="mr-3 w-10 float-left " />
				<p class="pt-2 font-bold italic">
					NFTL<span class="font-thin text-slate-100">Bookie</span>
				</p>
			</div>
		</div>
		<div class="-mt-32">
			<Hero3d />
		</div>
	</div>
	
	{#if !hasFinied}
	
	{#each sections.sections as {name, content},i}
	<Items entry={name}>
		{#each content as {start_match_hour, team1_name, team1_pourcentage, team1_cote, display_pourcentage, null_pourcentage, null_cote, team2_name, team2_pourcentage, team2_cote, ticket_price},i}
			<Bet {trad} {start_match_hour} {team1_name} {team1_pourcentage} {team1_cote} {display_pourcentage} {null_pourcentage} {null_cote} {team2_name} {team2_pourcentage} {team2_cote}/>
			
			
			
		{/each}
	</Items>
	{/each}

	{/if}
	<div class="w-full text-center mx-auto py-10">
		<p class="text-white tracking-widest">
			{#if !hasFinied}
				{trad.need_more}
			{:else}
				Need some $NFTL
			{/if}
		</p>
		<a href={trad.get_nftl_link}>
			<button
				class="bg-orange-500 text-white rounded-lg py-2 px-10  font-bold tracking-widest italic"
			>
				{trad.get_nftl}
			</button>
		</a>
	</div>
	<div class="flex items-center justify-center py-5">
		<TwitterLink link={trad.peko_link} displayName={peko} />
		<TwitterLink link={trad.finance_link} displayName={finance} />
		<!-- <TwitterLink link={trad.dragan_link} displayName={dragan} /> -->
	</div>
	<div class="text-sm p-3 font-light">
		{trad.conditions}
	</div>
</section>

<style>
	section {
		background: linear-gradient(24deg, rgba(33, 13, 1, 1) 58%, rgba(121, 60, 20, 1) 100%);
		font-family: 'Kanit', sans-serif;
	}
</style>
