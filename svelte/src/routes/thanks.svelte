<script>
	import Ticket from './components/thanks/Ticket.svelte';
	import { onMount } from 'svelte/internal';
	export let trad = {};
	export let ticket = {};
	onMount(() => {
		if (!window.location.hash) {
			window.location = window.location + '#loaded';
			window.location.reload();
		}
	});
</script>

<section>
	<Ticket {trad} {ticket}/>
</section>
