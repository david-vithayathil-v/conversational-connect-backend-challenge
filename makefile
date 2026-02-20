run:
	python manage.py runserver 0.0.0.0:8000

test:
	python manage.py test

test-pytest:
	pytest --disable-warnings

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations