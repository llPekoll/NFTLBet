<script>
	export let entry;
	let isOpen = true;
	const toggle = () => (isOpen = !isOpen);
</script>

<button on:click={toggle} aria-expanded={isOpen} class="ml-10"
	><svg
		class="inline"
		width="20"
		height="20"
		fill="none"
		stroke-linecap="round"
		stroke-linejoin="round"
		stroke-width="2"
		viewBox="0 0 24 24"
		stroke="currentColor"><path d="M9 5l7 7-7 7" /></svg
	>
	<p class="font-extralight inline">{entry}</p>
</button>
{#if isOpen}
	<slot />
{/if}

<style>
	button {
		display: block;
		font-size: 36px;
		cursor: pointer;
	}

	svg {
		transition: transform 0.2s ease-in;
	}

	[aria-expanded='true'] svg {
		transform: rotate(0.25turn);
	}
</style>
