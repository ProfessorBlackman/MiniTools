from prometheus_client import Gauge

from apps.logging_app.models.user_logs_model import UserLogsEntryModel

log_entries_metric = Gauge(
    'app_log_entries',
    'Number of log entries in the database',
    ['level']
)


def update_log_entries_metric():
    log_entries = UserLogsEntryModel.objects.all().values('level')
    log_entries_count = log_entries.count()
    print(f"this is log_entries_count : {log_entries_count}")

    # Reset the metric
    log_entries_metric.clear()

    # Set the metric value for each log level
    for entry in log_entries:
        log_entries_metric.labels(level=entry['level']).inc()
        print(f"this is entry: {entry}")

    # Set the total count
    log_entries_metric.labels(level='total').set(log_entries_count)
