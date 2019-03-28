pypy3 manage.py collectstatic --no-input
pypy3 manage.py migrate --no-input
celery -A bipad beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &
celery -A bipad worker --concurrency=4 -l info &
gunicorn --bind 0.0.0.0:8000 --workers=5 bipad.wsgi:application
