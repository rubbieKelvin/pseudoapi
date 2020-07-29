axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const isnone = (value) => (value === null || value === undefined);

const postrequest = (route, data) => {
	let promise = axios.post(route, data, {
		headers: {
			'X-Requested-With': 'XMLHttpRequest',
			'Accept': 'application/json'
		}
	});
	return promise;
};