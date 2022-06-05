<script lang="ts">
	import BgHero from './BgHero.svelte';
	import Countdown from './Countdown.svelte';
	import Hero3d from './Hero3d.svelte';
	import { onMount } from 'svelte/internal';

	import Counter from './Counter.svelte';
	import ButtonsVote from './ButtonsVote.svelte';
	import ButtonBuy from './ButtonBuy.svelte';
	import { goto } from '$app/navigation';
	const subContractAddress = '0x81663d5149cADBbc48CF1a7F21b05719Ee1420A9';
	const subContractAbi = [
		{
			constant: true,
			inputs: [],
			name: 'name',
			outputs: [
				{
					name: '',
					type: 'string'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: false,
			inputs: [
				{
					name: '_spender',
					type: 'address'
				},
				{
					name: '_value',
					type: 'uint256'
				}
			],
			name: 'approve',
			outputs: [
				{
					name: '',
					type: 'bool'
				}
			],
			payable: false,
			stateMutability: 'nonpayable',
			type: 'function'
		},
		{
			constant: true,
			inputs: [],
			name: 'totalSupply',
			outputs: [
				{
					name: '',
					type: 'uint256'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: false,
			inputs: [
				{
					name: '_from',
					type: 'address'
				},
				{
					name: '_to',
					type: 'address'
				},
				{
					name: '_value',
					type: 'uint256'
				}
			],
			name: 'transferFrom',
			outputs: [
				{
					name: '',
					type: 'bool'
				}
			],
			payable: false,
			stateMutability: 'nonpayable',
			type: 'function'
		},
		{
			constant: true,
			inputs: [],
			name: 'decimals',
			outputs: [
				{
					name: '',
					type: 'uint8'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: true,
			inputs: [
				{
					name: '_owner',
					type: 'address'
				}
			],
			name: 'balanceOf',
			outputs: [
				{
					name: 'balance',
					type: 'uint256'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: true,
			inputs: [],
			name: 'symbol',
			outputs: [
				{
					name: '',
					type: 'string'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			constant: false,
			inputs: [
				{
					name: '_to',
					type: 'address'
				},
				{
					name: '_value',
					type: 'uint256'
				}
			],
			name: 'transfer',
			outputs: [
				{
					name: '',
					type: 'bool'
				}
			],
			payable: false,
			stateMutability: 'nonpayable',
			type: 'function'
		},
		{
			constant: true,
			inputs: [
				{
					name: '_owner',
					type: 'address'
				},
				{
					name: '_spender',
					type: 'address'
				}
			],
			name: 'allowance',
			outputs: [
				{
					name: '',
					type: 'uint256'
				}
			],
			payable: false,
			stateMutability: 'view',
			type: 'function'
		},
		{
			payable: true,
			stateMutability: 'payable',
			type: 'fallback'
		},
		{
			anonymous: false,
			inputs: [
				{
					indexed: true,
					name: 'owner',
					type: 'address'
				},
				{
					indexed: true,
					name: 'spender',
					type: 'address'
				},
				{
					indexed: false,
					name: 'value',
					type: 'uint256'
				}
			],
			name: 'Approval',
			type: 'event'
		},
		{
			anonymous: false,
			inputs: [
				{
					indexed: true,
					name: 'from',
					type: 'address'
				},
				{
					indexed: true,
					name: 'to',
					type: 'address'
				},
				{
					indexed: false,
					name: 'value',
					type: 'uint256'
				}
			],
			name: 'Transfer',
			type: 'event'
		}
	];

	let provider;
	let amount = 'Connect';
	let account;
	let ticktNb;
	let SendTransactionNFTL;
	let selecedTeam = 1;
	onMount(async () => {
		provider = new ethers.providers.Web3Provider(window.ethereum);
		SendTransactionNFTL = async () => {
			// console.log('sent')
			goto('/thanks');
		};
	});
	//     }
	const connect = async () => {
		// console.log(provider);
		const accounts = await window.ethereum
			.request({
				method: 'eth_requestAccounts'
			})
			.catch((err) => {
				console.log(err.code);
			});

		account = accounts[0];
		console.log(account);
		let subContract = new ethers.Contract(subContractAddress, subContractAbi, provider);
		let bal = await subContract.balanceOf(account);
		amount = bal.toString() / Math.pow(10, 9);
		amount = `${amount.toFixed(2)}`;
	};
	const selectTeam = (team) => {
		console.log(team);
	};
</script>

<section class="text-slate-300">
	<div>
		<div class="opacity-20">
			<!-- <BgHero /> -->
		</div>
		<div class="p-5 ">
			<button
				class=" bg-orange-500 float-right px-8 rounded-full border-2 border-orange-600 text-slate-100 "
				on:click={connect}
			>
				{#if amount !== 'Connect'}
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
		<div class="text-center font-thin -mt-16">End of the game in:</div>
		<Countdown />
	</div>

	<div class="py-20 flex items-center justify-center">
		<div class="mx-10 text-center">
			<ButtonsVote color="#f1c40f" text="Madrid" bind:selecedTeam teamNb="1" />
			<p class=" font-thin text-xs -mb-1.5">cote:</p>
			<p class="font-bold text-xl">3,4</p>
		</div>
		<div class="mx-10 text-center">
			<ButtonsVote color="rgb(2, 64, 2)" text="null" bind:selecedTeam teamNb="3" />
			<p class=" font-thin text-xs -mb-1.5">cote:</p>
			<p class="font-bold text-xl">2,2</p>
		</div>
		<div class="mx-10 text-center">
			<ButtonsVote color="#e74c3c" text="LiverPool" bind:selecedTeam teamNb="2" />
			<p class=" font-thin text-xs -mb-1.5">cote:</p>
			<p class="font-bold text-xl">1,2</p>
		</div>
	</div>
	<Counter bind:ticktNb />
	<div class="text-center text-white pt-2 font-thin text-sm">
		price:
		<!-- {trad.ticket_price}: ${lottery.ticket_price}NFTL -->
	</div>
	<div class="text-center text-white font-bold text-3xl -mt-2 italic">
		{ticktNb * 300}<span class="font-semibold italic text-base ">$NFTL</span>
	</div>

	<div class="text-center px-30  py-5 ">
		<button on:click={SendTransactionNFTL} class="drop-shadow-md">
			<ButtonBuy />
		</button>
	</div>
	<div class="w-full text-center mx-auto py-10">
		<p class="text-white tracking-widest">
			need more $NFTL?
			<!-- {trad.need_more} -->
		</p>
		<!-- <a href={trad.get_nftl_link}> -->
		<a href="/">
			<button
				class="bg-orange-500 text-white rounded-lg py-2 px-10  font-bold tracking-widest italic"
			>
				<!-- {trad.get_nftl} -->
				Get $NFTL
			</button>
		</a>
	</div>
	<div class="flex py-5">
		<div class="flex items-end justify-start px-10">
			<div class="w-5 text-white mr-2">
				<svg viewBox="0 0 448 512"
					><path
						fill="currentColor"
						d="M400 32H48C21.5 32 0 53.5 0 80v352c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V80c0-26.5-21.5-48-48-48zm-48.9 158.8c.2 2.8.2 5.7.2 8.5c0 86.7-66 186.6-186.6 186.6c-37.2 0-71.7-10.8-100.7-29.4c5.3.6 10.4.8 15.8.8c30.7 0 58.9-10.4 81.4-28c-28.8-.6-53-19.5-61.3-45.5c10.1 1.5 19.2 1.5 29.6-1.2c-30-6.1-52.5-32.5-52.5-64.4v-.8c8.7 4.9 18.9 7.9 29.6 8.3a65.447 65.447 0 0 1-29.2-54.6c0-12.2 3.2-23.4 8.9-33.1c32.3 39.8 80.8 65.8 135.2 68.6c-9.3-44.5 24-80.6 64-80.6c18.9 0 35.9 7.9 47.9 20.7c14.8-2.8 29-8.3 41.6-15.8c-4.9 15.2-15.2 28-28.8 36.1c13.2-1.4 26-5.1 37.8-10.2c-8.9 13.1-20.1 24.7-32.9 34z"
					/></svg
				>
			</div>
			<p class="inline italic">@llPekoll</p>
		</div>
		<div class="flex items-center justify-center px-10">
			<div class="w-5 text-white mr-2">
				<svg viewBox="0 0 448 512"
					><path
						fill="currentColor"
						d="M400 32H48C21.5 32 0 53.5 0 80v352c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V80c0-26.5-21.5-48-48-48zm-48.9 158.8c.2 2.8.2 5.7.2 8.5c0 86.7-66 186.6-186.6 186.6c-37.2 0-71.7-10.8-100.7-29.4c5.3.6 10.4.8 15.8.8c30.7 0 58.9-10.4 81.4-28c-28.8-.6-53-19.5-61.3-45.5c10.1 1.5 19.2 1.5 29.6-1.2c-30-6.1-52.5-32.5-52.5-64.4v-.8c8.7 4.9 18.9 7.9 29.6 8.3a65.447 65.447 0 0 1-29.2-54.6c0-12.2 3.2-23.4 8.9-33.1c32.3 39.8 80.8 65.8 135.2 68.6c-9.3-44.5 24-80.6 64-80.6c18.9 0 35.9 7.9 47.9 20.7c14.8-2.8 29-8.3 41.6-15.8c-4.9 15.2-15.2 28-28.8 36.1c13.2-1.4 26-5.1 37.8-10.2c-8.9 13.1-20.1 24.7-32.9 34z"
					/></svg
				>
			</div>
			<p class="inline italic">@FinanceFr</p>
		</div>
		<div class="flex items-center justify-center px-10">
			<div class="w-5 text-white mr-2">
				<svg viewBox="0 0 448 512"
					><path
						fill="currentColor"
						d="M400 32H48C21.5 32 0 53.5 0 80v352c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V80c0-26.5-21.5-48-48-48zm-48.9 158.8c.2 2.8.2 5.7.2 8.5c0 86.7-66 186.6-186.6 186.6c-37.2 0-71.7-10.8-100.7-29.4c5.3.6 10.4.8 15.8.8c30.7 0 58.9-10.4 81.4-28c-28.8-.6-53-19.5-61.3-45.5c10.1 1.5 19.2 1.5 29.6-1.2c-30-6.1-52.5-32.5-52.5-64.4v-.8c8.7 4.9 18.9 7.9 29.6 8.3a65.447 65.447 0 0 1-29.2-54.6c0-12.2 3.2-23.4 8.9-33.1c32.3 39.8 80.8 65.8 135.2 68.6c-9.3-44.5 24-80.6 64-80.6c18.9 0 35.9 7.9 47.9 20.7c14.8-2.8 29-8.3 41.6-15.8c-4.9 15.2-15.2 28-28.8 36.1c13.2-1.4 26-5.1 37.8-10.2c-8.9 13.1-20.1 24.7-32.9 34z"
					/></svg
				>
			</div>
			<p class="inline italic ">@Dragan</p>
		</div>
	</div>
</section>

<style>
	section {
		background: linear-gradient(24deg, rgba(33, 13, 1, 1) 58%, rgba(121, 60, 20, 1) 100%);
		font-family: 'Kanit', sans-serif;
	}
</style>
