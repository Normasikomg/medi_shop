import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineautoshop.settings')

app = Celery('onlineautoshop')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-report_every_single_minute": {
        'task': 'publisher.tasks.send_view_count_report',
        'schedule': crontab(),
    },
}
