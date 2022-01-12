// this function will grab the contents of the ""
async function talkToRobot() {

	// ge
	let prompt = document.getElementById('input').value

	console.log(prompt)
	
	// Create WebSocket connection.
	const request = await fetch("http://10.42.0.1:8000/ask;'" + prompt + "'", {
		method: 'GET'
	})

	document.getElementById('output').textContent = 'sending request'

	const value = await request.text()
	
	document.getElementById('output').textContent = value

}
