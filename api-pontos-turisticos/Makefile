make:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

createsuperuser:
	python3 manage.py createsuperuser

runserver:
	python3 manage.py runserver localhost:9008

runserver_production:
	python3 manage.py runserver localhost:9008 --settings=config.settings.production

setup:
	python3 manage.py migrate
	python3 manage.py createsuperuser --username=admin --email=admin@admin.com --noinput
