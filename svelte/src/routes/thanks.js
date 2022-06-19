/** @type {import('@sveltejs/kit').RequestHandler} */

export async function get({ request, params, url }) {
	const ticketNb = url.searchParams.get('id');
	const env = import.meta.env;
	const res = await fetch(`${env.VITE_BACKEND_DNS}/trads`);
	const res2 = await fetch(`${env.VITE_BACKEND_DNS}/ticket/${ticketNb}`);
	const trad = await res.json();
	const ticket = await res2.json();
	return {
		body: {
			trad,
			ticket
		}
	};
}
