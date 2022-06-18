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
			match,
		}
	};
}

export async function post({ request }) {
	const env = import.meta.env;
	const url = `${env.VITE_BACKEND_DNS}/ticket/`;
	const body = await request.json();
	try {
		const response = await fetch(url, { method: 'POST', body: JSON.stringify(body) });
		return {
			status: 200,
			body: response.data
		};
	} catch (error) {
		return { status: 500, body: error };
	}
}
