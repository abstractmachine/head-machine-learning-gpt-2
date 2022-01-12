
async function talkToRobot() {

	const prompt = "HAMLET:"
	// Create WebSocket connection.
	const request = await fetch("http://localhost:8000/ask;" + prompt, {
		method: 'GET'
	})

	output = document.getElementById('output')

	output.textContent = 'sending request'

	const value = await request.text()
	
	output.textContent = value

}
