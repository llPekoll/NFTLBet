<script>
	import Ticket from './components/thanks/Ticket.svelte';
    import { onMount } from 'svelte/internal';
    onMount(() => {
        if(!window.location.hash) {
            window.location = window.location + '#loaded';
            window.location.reload();
    }
    });
</script>

<section>
	<Ticket />
</section>
