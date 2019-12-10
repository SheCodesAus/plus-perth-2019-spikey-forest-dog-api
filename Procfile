release: python manage.py migrate

web: waitress-serve --port=$PORT API.wsgi:application