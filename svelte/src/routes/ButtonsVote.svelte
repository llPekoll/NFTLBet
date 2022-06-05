<script lang="ts">
	export let color: string;
	export let text: string = 'willmase';
	export let selecedTeam: number;
	export let teamNb: number;
	const clicked = () => {
		console.log(selecedTeam);
		console.log(teamNb);
		selecedTeam = teamNb;
	};
	// $: selecedTeam = 33
</script>

<button
	style="--theme-color: {color}"
	on:click={() => {
		selecedTeam = teamNb;
	}}
	class:selected={selecedTeam == teamNb}
	class="btn py-3 px-10 extra text-white"
	>{text}
</button>

<style>
	.btn {
		box-sizing: border-box;
		-webkit-appearance: none;
		-moz-appearance: none;
		appearance: none;
		background-color: transparent;
		border: 2px solid #e74c3c;
		border-radius: 0.6em;
		/* color: #e74c3c; */
		cursor: pointer;
		display: flex;
		align-self: center;
		font-size: 1rem;
		font-weight: 400;
		line-height: 1;
		font-weight: 700;
	}
	.btn:hover,
	.btn:focus {
		outline: 0;
	}

	.selected {
		background-color: var(--theme-color);
	}
	.extra {
		border-color: var(--theme-color);

		background-image: linear-gradient(45deg, var(--theme-color) 50%, transparent 50%);
		background-position: 100%;
		background-size: 400%;
		transition: background 300ms ease-in-out;
	}

	.btn:hover {
		background-position: 0;
	}
</style>
