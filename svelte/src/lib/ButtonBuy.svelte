<script lang="ts">
	export let trad:{[string]:string};
	export let display_pourcentage:boolean
</script>

<button class="{display_pourcentage?'mt-0':'mt-7'} py-1.5 px-4 bg-blue-600 rounded text-xs text-white mx-5 ">
		{trad.buy_ticket}
</button>