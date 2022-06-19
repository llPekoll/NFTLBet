/** @type {import('@sveltejs/kit').RequestHandler} */

export async function get() {
	const env = import.meta.env;
	const res = await fetch(`${env.VITE_BACKEND_DNS}/trads`);
	const res2 = await fetch(`${env.VITE_BACKEND_DNS}/match`);
	const trad = await res.json();
	const match = await res2.json();
	return {
		body: {
			trad,
			match
		}
	};
}
