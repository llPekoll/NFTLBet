<script lang="ts">
	import { onMount } from 'svelte';
    // import {FlipDown} from 'flipdown/src/flipdown.js';

	onMount(() => {
		var twoDaysFromNow = new Date().getTime() / 1000 + 86400 * 2 + 1;
		var flipdown = new FlipDown(twoDaysFromNow);
		flipdown.start();
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
