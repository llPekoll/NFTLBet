<script lang="ts">
	export let color: string;
	export let text: string = 'willmase';
	export let selecedTeam: number;
	export let teamNb: number;
    export let pourcent: number;
    export let cote:number;
    const clicked = () => {
		console.log(selecedTeam);
		console.log(teamNb);
		selecedTeam = teamNb;
	};
	// $: selecedTeam = 33
</script>
<p class="font-light italic text-xs ">cote:</p>
<p class="text-white font-bold -mt-2 text-lg">{cote}</p>
<button
style="--theme-color: {color}"
on:click={() => {
    selecedTeam = teamNb;
}}
	class:selected={selecedTeam == teamNb}
	class="btn py-3 px-10 extra text-white"
	>
    <p class="text-xl">{text}</p>
</button>
<div class="flex py-2">
    <div class="text-xs">{pourcent}%</div>
    <div class=" jj w-full bg-gray-600 rounded-full h-1.5 ml-1">
      <div class="bg-gray-200 h-1.5 rounded-full " style="width: {pourcent}% "></div>
    </div>
</div>

<style>
    .jj{
        margin-top: 0.3rem
    }
	.btn {
		box-sizing: border-box;
		-webkit-appearance: none;
		-moz-appearance: none;
		appearance: none;
		background-color: transparent;
		border: 2px solid #e74c3c;
		border-radius: 0.6em;
		cursor: pointer;
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
