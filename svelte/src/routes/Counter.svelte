<script>
	import { spring } from 'svelte/motion';
	export let ticktNb = 1;

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

<div class="counter text-white  w-52 rounded-lg text-center mx-auto bg-orange-500">
	<button on:click={() => (ticktNb -= 1)} aria-label="Decrease the counter by one">
		<svg aria-hidden="true" viewBox="0 0 1 1">
			<path d="M0,0.5 L1,0.5" />
		</svg>
	</button>

	<div class="counter-viewport">
		<div class="counter-digits" style="transform: translate(0, {100 * offset}%)">
			<strong class="hidden" aria-hidden="true">{Math.floor($displayed_count + 1)}</strong>
			<strong>{Math.floor($displayed_count)}</strong>
		</div>
	</div>

	<button
		on:click={() => (ticktNb += 1)}
		aria-label="Increase the counter by one"
		class="text-white"
	>
		<svg aria-hidden="true" viewBox="0 0 1 1" fill="black">
			<path d="M0,0.5 L1,0.5 M0.5,0 L0.5,1" />
		</svg>
	</button>
</div>

<style>
	.counter {
		display: flex;
		border-top: 1px solid rgba(0, 0, 0, 0.1);
		border-bottom: 1px solid rgba(0, 0, 0, 0.1);
	}

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
		font-size: 2rem;
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
		height: 3.5em;
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
		font-size: 3rem;
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
