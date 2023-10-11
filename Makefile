dev:
	poetry run python manage.py runserver

shell:
	poetry run python manage.py shell

migrate:
	poetry run python manage.py migrate

get migr:
	python manage.py makemigrations
