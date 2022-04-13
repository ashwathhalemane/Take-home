1. Created a web backend using flask
2. Used pytest to write unit tests and included as pre-commit hook
3. Used Docker to containarize the application

4. Usage:
	
	docker run -d -p 5000:5000 python-docker
	
	Make a get request to http://127.0.0.1:5000/health
		returns json with value 200 	
	Make a curl request for /detect_intent endpoint which only supports post method
		returns json with utterance and intent
	
	
	
	
	
