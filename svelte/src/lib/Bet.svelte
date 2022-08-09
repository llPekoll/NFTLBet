<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte/internal';

	import { subContractAbi } from './abi';
    import {subContractAddress} from './subContractAddress'

	import ButtonsVote from './ButtonsVote.svelte';
	import Counter from './Counter.svelte';
	import ButtonBuy from './ButtonBuy.svelte';

	export let trad: {
		[string]: string;
	};
	export let start_match_hour: string;
	export let team1_name: string;
	export let team1_cote: string;
	export let team1_wallet: string;
	export let team1_pourcentage: string;
	export let team2_name: string;
	export let team2_cote: string;
	export let team2_wallet: string;
	export let team2_pourcentage: string;
	export let null_pourcentage: string;
	export let null_cote: string;
	export let null_wallet: string;
	export let display_pourcentage: string;
	export let ticket_price: number;
    export let id:number;

    let selecedTeam: string = '1';
	let ticktNb: number = 1;
	let SendTransactionNFTL;
	onMount(async () => {
		const provider = new ethers.providers.Web3Provider(window.ethereum);
		SendTransactionNFTL = async () => {
            const bet_value = ticktNb * ticket_price;
            let wallet: string = 'sako';
            if (selecedTeam === '1') {
                wallet = team1_wallet;
            } else if (selecedTeam === '2') {
                wallet = team2_wallet;
            } else if (selecedTeam === '3') {
                wallet = null_wallet;
            }
			let subContract = new ethers.Contract(
				subContractAddress,
				subContractAbi,
				provider.getSigner()
			);
			const toPay = ethers.utils.parseUnits(`${bet_value}.0`, 9);
			try {
				let tx = await subContract.transfer(wallet, toPay);
			} catch (e) {
				console.log('error', e);
				return 0;
			}

			const data = {
				id,
				wallet,
				amount: bet_value
			};
			const ret = await fetch(`/query/ticket`, {
				method: 'post',
				body: JSON.stringify(data)
			});
			const ticket = await ret.json();
			goto(`/thanks?id=${ticket.id}`);
		};
	});
    let countdown;
    let countDownDate = new Date(start_match_hour).getTime();
    let x = setInterval(function () {
		let now = new Date().getTime();
		let distance = countDownDate - now;
		let days = Math.floor(distance / (1000 * 60 * 60 * 24));
		let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		let seconds = Math.floor((distance % (1000 * 60)) / 1000);
		countdown = `${days}d ${hours}h  ${minutes}m  ${seconds}s`;
		if (distance < 0) {
			clearInterval(x);
			countdown = '!!!!! Done !!!!!';
		}
	}, 1000);
</script>

<div class="text-center font-thin mt-2">
	{trad.end_game}: <span class="font-bold italic">{countdown}</span>
</div>

<div class="md:flex flex-wrap items-center justify-center">
	<div class="mx-1 text-center">
		<ButtonsVote
			color="#f1c40f"
			text={team1_name}
			bind:selecedTeam
			teamNb="1"
			pourcent={team1_pourcentage}
			cote={team1_cote}
			display={display_pourcentage}
		/>
	</div>
	<div class="mx-1 text-center">
		<ButtonsVote
			color="rgb(2, 64, 2)"
			text={trad.null}
			bind:selecedTeam
			teamNb="3"
			pourcent={null_pourcentage}
			cote={null_cote}
			display={display_pourcentage}
		/>
	</div>
	<div class="mx-1 text-center">
		<ButtonsVote
			color="#e74c3c"
			text={team2_name}
			bind:selecedTeam
			teamNb="2"
			pourcent={team2_pourcentage}
			cote={team2_cote}
			display={display_pourcentage}
		/>
	</div>
	<Counter bind:ticktNb {ticket_price} {display_pourcentage}/>
	<div class="text-center mx-auto md:mx-0 md:text-left ">
        <button on:click={SendTransactionNFTL} class="drop-shadow-md">
			<ButtonBuy {trad} {display_pourcentage}/>
		</button>
	</div>
</div>
