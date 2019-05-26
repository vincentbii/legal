release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn gs.wsgi --log-file -
