run:
	flask --app app.main run --debug --port 8000

test:
	pytest --disable-warnings