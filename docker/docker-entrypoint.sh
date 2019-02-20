python3 -m pip install -r requirements.txt
python manage.py migrate --no-input
celery -A bipad beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &
celery -A bipad worker --concurrency=4 -l info &
python manage.py runserver 0.0.0.0:8000
