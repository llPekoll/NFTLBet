<script>
	import { spring } from 'svelte/motion';
	export let ticktNb = 1;
	export let ticket_price;
	export let display_pourcentage;

	const displayed_count = spring();
	$: displayed_count.set(ticktNb);
	$: offset = modulo($displayed_count, 1);
	$: if (ticktNb < 1) {
		ticktNb = 1;
	}
	/**
	 * @param {number} n
	 * @param {number} m
	 */
	function modulo(n, m) {
		// handle negative numbers
		return ((n % m) + m) % m;
	}
</script>
<div class='mx-10 {display_pourcentage?'-mt-7':'mt-0'}'>
	
	<div class=" text-white font-bold text-lg italic md:mx-0 md:text-left mx-auto text-center">
		{ticktNb * ticket_price}<span class="font-thin italic text-xs ">$NFTL</span>
	</div>
	<div class="flex counter text-white w-20 h-7 rounded bg-orange-500 mx-auto text-center">
		<button on:click={() => (ticktNb -= 1)} aria-label="Decrease the counter by one text-slate-500">
			<span class="text-slate-900">- </span>
		</button>
		
		<div class="counter-viewport">
			<div class="counter-digits" style="transform: translate(0, {100 * offset}%)">
				<strong class="hidden" aria-hidden="true">{Math.floor($displayed_count + 1)}</strong>
				<strong class="text">{Math.floor($displayed_count)}</strong>
			</div>
		</div>
		
		<button
		on:click={() => (ticktNb += 1)}
		aria-label="Increase the counter by one"
		class="text-white"
		>
		<span class="text-slate-900">+</span>
	</button>
	
</div>

</div>

<style>
	
	.counter button {
		width: 2em;
		padding: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 0;
		background-color: transparent;
		touch-action: manipulation;
		color: var(--text-color);
	}

	.counter button:hover {
		background-color: var(--secondary-color);
	}

	svg {
		width: 25%;
		height: 25%;
		fill: black;
	}

	path {
		vector-effect: non-scaling-stroke;
		stroke-width: 2px;
		stroke: black;
	}

	.counter-viewport {
		width: 8em;
		
		overflow: hidden;
		text-align: center;
		position: relative;
	}

	.counter-viewport strong {
		position: absolute;
		display: flex;
		width: 100%;
		height: 100%;
		font-weight: 400;
		color: var(--accent-color);
		align-items: center;
		justify-content: center;
	}

	.counter-digits {
		position: absolute;
		width: 100%;
		height: 100%;
	}

	.hidden {
		top: -100%;
		user-select: none;
	}
</style>
