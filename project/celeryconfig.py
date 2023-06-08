from decouple import config
from datetime import timedelta


CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
# CELERY_WORKER_MAX_TASKS_PER_CHILD = 2
CELERY_RESULT_EXTENDED = True
CELERY_RESULT_BACKEND_OPTIONS = {"include_meta": True}
CELERY_TASK_RESULT_EXPIRES = timedelta(days=1)