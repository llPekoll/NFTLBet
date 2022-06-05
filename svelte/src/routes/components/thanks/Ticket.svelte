<script lang="ts">
	import { onMount } from 'svelte';
	import { jsPDF } from 'jspdf';

	let divToPdf;
	onMount(() => {
		JsBarcode('#barcode')
			.EAN13('493107890128', { height: 40, fontSize: 18, textMargin: 0 })
			.render();

		divToPdf = () => {
			var doc = new jsPDF();
			const content =
				`<html><head><title>NFTLBookie</title></head><body>` +
				document.getElementById('base').innerHTML +
				`</body></html>`;
			html2canvas(document.querySelector('#capture')).then((canvas) => {
				document.body.appendChild(canvas);
			});
		};
	});
</script>

<!--
Inspired by: https://dribbble.com/shots/1166639-Movie-Ticket/attachments/152161
-->
<section id="base" class=" flex items-center justify-center text-stone-700">
	<div on:click={divToPdf} id="ticket" class="ticket --flex-column ">
		<div class="top --flex-column">
			<div>
				<img src="NFTL.webp" alt="logo" class="mr-2 w-7 float-left ml-3" />
				<p class="pt-6 font-bold italic text-sm">
					NFTL<span class="font-thin text-slate-700">Bookie</span>
				</p>
			</div>
			<div class="tourname clear-both ml-3 text-xl font-bold italic">
				Madrid <span class="font-thin text-sm non-italic"> vs</span> LiverPool
			</div>
			<img src="/nftl.png" alt="ticket illustration" />
			<div class="deetz --flex-row-j!sb ml-3">
				<div class="event --flex-column">
					<p class="font-semithin text-sm">
						You betted for
						<br />
					</p>
					<p class=" font-bold text-xl italic -mt-2 pb-5">Madrid Winner!</p>
					<div class="text-xs">0xb47e..93BBB</div>
				</div>
				<div class="price --flex-column text-right mr-3">
					<p class="italic text-xl font-bold">
						<span class="text-sm font-normal">$NFTL</span>30000
					</p>
				</div>
			</div>
		</div>
		<div class="rip " />
		<div class="bottom --flex-row-j!sb pl-1">
			<svg id="barcode" />
		</div>
	</div>
</section>

<style>
	section {
		background: linear-gradient(24deg, rgba(33, 13, 1, 1) 58%, rgba(121, 60, 20, 1) 100%);
		height: 100vh;
	}
	.ticket {
		filter: drop-shadow(1px 1px 3px rgba(0, 0, 0, 0.3));
	}
	.ticket {
		width: 255px;
	}

	.ticket .top img,
	.ticket .bottom img {
		padding: 18px 0;
	}
	.ticket .top,
	.ticket .bottom,
	.ticket .rip {
		background-color: #fff;
	}
	.ticket .top {
		border-top-right-radius: 5px;
		border-top-left-radius: 5px;
	}
	.ticket .top .deetz {
		padding-bottom: 10px !important;
	}
	.ticket .bottom {
		border-bottom-right-radius: 5px;
		border-bottom-left-radius: 5px;
	}

	.ticket .rip {
		height: 20px;
		margin: 0 10px;
		background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAYAAAACCAYAAAB7Xa1eAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuOWwzfk4AAAAaSURBVBhXY5g7f97/2XPn/AcCBmSMQ+I/AwB2eyNBlrqzUQAAAABJRU5ErkJggg==);
		background-size: 4px 2px;
		background-repeat: repeat-x;
		background-position: center;
		position: relative;
		box-shadow: 0 1px 0 0 #fff, 0 -1px 0 0 #fff;
	}
	.ticket .rip:before,
	.ticket .rip:after {
		content: '';
		position: absolute;
		width: 20px;
		height: 20px;
		top: 50%;
		transform: translate(-50%, -50%) rotate(45deg) scale(2);
		border: 5px solid transparent;
		border-top-color: #fff;
		border-right-color: #fff;
		border-radius: 100%;
		pointer-events: none;
	}
	.ticket .rip:before {
		left: -10px;
	}
	.ticket .rip:after {
		transform: translate(-100%, -50%) rotate(225deg) scale(2);
		right: -40px;
	}
</style>
