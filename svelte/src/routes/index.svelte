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
			<ButtonsVote color="#f1c40f" text="Madrid" bind:selecedTeam teamNb="1" pourcent=20 cote=3.4/>
		</div>
		<div class="mx-10 text-center">
			<ButtonsVote color="rgb(2, 64, 2)" text="null" bind:selecedTeam teamNb="3" pourcent=10 cote=2/>
		</div>
		<div class="mx-10 text-center">
			<ButtonsVote color="#e74c3c" text="LiverPool" bind:selecedTeam teamNb="2" pourcent=70 cote=1.2/>
		</div>
	</div>
	<Counter bind:ticktNb />
	<div class="text-center text-white pt-2 font-thin text-xs">
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
	<div class="flex items-center justify-center py-5">
		<TwitterLink link="https://twitter.com/llpekoll" displayName="@peko" />
		<TwitterLink link="https://twitter.com/FinanceFr" displayName="@FinanceFr" />
		<TwitterLink link="https://twitter.com/dragan" displayName="@Dragan" />
	</div>
</section>

<style>
	section {
		background: linear-gradient(24deg, rgba(33, 13, 1, 1) 58%, rgba(121, 60, 20, 1) 100%);
		font-family: 'Kanit', sans-serif;
	}
</style>
