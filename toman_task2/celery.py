import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toman_task2.settings')

app = Celery('toman_task2')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.worker_prefetch_multiplier = 1
app.conf.broker_connection_retry_on_startup = True
app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'change_status_expired_request': {
        'task': 'request_manager.tasks.change_status_expired_request',
        'schedule': crontab(minute='*'),
    },
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
