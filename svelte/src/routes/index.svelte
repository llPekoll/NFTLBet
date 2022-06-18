<script lang="ts">
	import BgHero from './BgHero.svelte';
	import Countdown from './Countdown.svelte';
	import Hero3d from './Hero3d.svelte';
	import { onMount } from 'svelte/internal';

	import Counter from './Counter.svelte';
	import ButtonsVote from './ButtonsVote.svelte';
	import ButtonBuy from './ButtonBuy.svelte';
	import { goto } from '$app/navigation';
	import TwitterLink from './components/home/TwitterLink.svelte';

	export let trad = {};
	export let match = {};
	export let abi = {};

	const subContractAddress = '0x81663d5149cADBbc48CF1a7F21b05719Ee1420A9';

	let provider;
	let amount = trad.connect;
	let account;
	let ticktNb;
	let SendTransactionNFTL;
	let selecedTeam = '1';
	let hasFinied = false;
	onMount(async () => {
		provider = new ethers.providers.Web3Provider(window.ethereum);
		SendTransactionNFTL = async () => {
			let subContract = new ethers.Contract(
				subContractAddress,
				subContractAbi,
				provider.getSigner()
			);
			const bet_value = ticktNb * match.ticket_price;
			const toPay = ethers.utils.parseUnits(`${bet_value}.0`, 9);
			let wallet: string = 'sako';
			if (selecedTeam === '1') {
				wallet = match.team1_wallet;
			} else if (selecedTeam === '2') {
				wallet = match.team2_wallet;
			} else if (selecedTeam === '3') {
				wallet = match.null_wallet;
			}
			try {
				let tx = await subContract.transfer(wallet, toPay);
			} catch (e) {
				console.log('error', e);
				return 0;
			}
			const data = {
				wallet,
				amount: bet_value
			};
			const ret = await fetch(`/`, {
				method: 'post',
				body: JSON.stringify(data)
			});
			const ticket = ret.json()
			goto(`/thanks?id=${ticket.id}`);
		};
	});
	//     }
	const connect = async () => {
		const accounts = await window.ethereum
			.request({
				method: 'eth_requestAccounts'
			})
			.catch((err) => {
				console.log(err.code);
			});

		account = accounts[0];
		console.log(abi);
		let subContract = new ethers.Contract(subContractAddress, abi, provider);
		console.log('subContract')
		console.log(subContract)
		let bal = await subContract.balanceOf(account);
		amount = bal.toString() / Math.pow(10, 9);
		amount = `${amount.toFixed(2)}`;
	};
	const peko = `@${trad.peko}`;
	const finance = `@${trad.finance}`;
	// const dragan = `@${trad.dragan}`;
	let fullHight = '';
	$: if(hasFinied){
		fullHight ="h-screen"
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
		{#if !hasFinied}
			<div class="text-center font-thin -mt-16">{trad.end_game}:</div>
		<Countdown time={match.start_match_hour} bind:hasFinied/>
		{/if}
	</div>

	{#if !hasFinied}
	<div class="py-20 md:flex flex-wrap items-center justify-center">
		<div class="mx-10 text-center">
			<ButtonsVote
				color="#f1c40f"
				text={match.team1_name}
				bind:selecedTeam
				teamNb="1"
				pourcent={match.team1_pourcentage}
				cote={match.team1_cote}
				display={match.display_pourcentage}
			/>
		</div>
		<div class="mx-10 text-center">
			<ButtonsVote
				color="rgb(2, 64, 2)"
				text="null"
				bind:selecedTeam
				teamNb="3"
				pourcent={match.null_pourcentage}
				cote={match.null_cote}
				display={match.display_pourcentage}
			/>
		</div>
		<div class="mx-10 text-center">
			<ButtonsVote
				color="#e74c3c"
				text={match.team2_name}
				bind:selecedTeam
				teamNb="2"
				pourcent={match.team2_pourcentage}
				cote={match.team2_cote}
				display={match.display_pourcentage}
			/>
		</div>
	</div>
	<Counter bind:ticktNb />
	<div class="text-center text-white pt-2 font-thin text-xs">
		{trad.price}:
	</div>
	<div class="text-center text-white font-bold text-3xl -mt-2 italic">
		{ticktNb * match.ticket_price}<span class="font-semibold italic text-base ">$NFTL</span>
	</div>
		<div class="text-center px-30  py-5 ">
			<button on:click={SendTransactionNFTL} class="drop-shadow-md">
				<ButtonBuy {trad} />
			</button>
		</div>
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
