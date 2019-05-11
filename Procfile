release: python manage.py migrate
release: python manage.py createsuperuser --email biivincent4@gmail.com --username admin
web: gunicorn gs.wsgi --log-file -
