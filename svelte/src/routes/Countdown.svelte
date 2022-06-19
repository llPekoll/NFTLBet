<script lang="ts">
	import { onMount } from 'svelte';
	export let time;
	export let hasFinied;

	onMount(() => {
		var flipdown = new FlipDown(time).start().ifEnded(() => {
			hasFinied = true;
			console.log('The countdown has ended!');
		});
	});
</script>

<svelte:head>
	<script type="text/javascript" src="/flipdown.min.js"></script>
	<link rel="stylesheet" href="/flipdown.min.css" />
</svelte:head>

<section class="w-full flex items-center -mt-5">
	<div id="flipdown" class="flipdown flipdown__theme-light flex items-center justify-center" />
</section>

<style>
	#flipdown {
		width: 100%;
		transform: scale(0.5);
	}
</style>
