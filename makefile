run:
	uvicorn app.main:app --reload

test:
	pytest --disable-warnings