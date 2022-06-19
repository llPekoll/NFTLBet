/** @type {import('@sveltejs/kit').RequestHandler} */

export async function post({ request }) {
	const env = import.meta.env;
	const url = `${env.VITE_BACKEND_DNS}/ticket/`;
	const body = await request.json();
	try {
		const response = await fetch(url, { method: 'POST', body: JSON.stringify(body) });
		const jose = await response.json();
		console.log(jose);
		return {
			status: 200,
			body: jose
		};
	} catch (error) {
		return { status: 500, body: error };
	}
}
