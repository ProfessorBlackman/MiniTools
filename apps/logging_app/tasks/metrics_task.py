from celery import shared_task

from apps.logging_app.services.metrics_for_prometheus import update_log_entries_metric


@shared_task
def update_log_entries_metric_task():
    update_log_entries_metric()
