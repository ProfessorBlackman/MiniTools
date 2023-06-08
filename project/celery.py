"""This file contains celery configurations and initialization. """
import os
from celery import Celery
from celery.events.state import State
from celery.signals import before_task_publish, task_prerun, task_postrun, task_success, after_task_publish, \
    task_failure, task_retry, task_internal_error
from utils.logging.loggers import tasks_logger, tasks_critical_logger, tasks_error_logger, tasks_warning_logger

state = State()
# logging.basicConfig(filename='tasks.log', level=logging.INFO)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
app = Celery("MiniTools")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# -------------------------------------------------Task Logs------------------------------------------------------------
# logs for when a task is published
@before_task_publish.connect
def log_before_task_is_published(sender=None, body=None, **kwargs):
    tasks_logger.info(f'Task {sender} is ready to be published to queue')


# logs for after a task is run
@after_task_publish.connect
def log_after_task_is_published(sender=None, body=None, **kwargs):
    tasks_logger.info(f'Task {sender} has been published to queue')


# logs for when a task is about to run
@task_prerun.connect
def log_before_task_is_run(sender=None, task_id=None, task=None, **kwargs):
    tasks_logger.info(f'Task {sender} with task id {task_id} is ready to run')


# logs for after a task is run
@task_postrun.connect
def log_after_task_is_run(sender=None, task_id=None, task=None, **kwargs):
    tasks_logger.info(f'Task {sender} with task id {task_id} is done running')


# logs for when a task is executed successfully
@task_success.connect
def log_when_task_is_successful(sender=None, result=None, **kwargs):
    tasks_logger.info(f'Task {sender} is successful. \n This is the result: {result}')


# logs for when a task fails
@task_failure.connect
def log_when_task_fails(sender=None, task_id=None, exception=None, **kwargs):
    tasks_error_logger.error(
        f'Task {sender} with task id {task_id} failed with the following exception: str({exception})')


# logs for when a task is retried after failure
@task_retry.connect
def log_when_task_is_retrying(sender=None, reason=None, request=None, **kwargs):
    tasks_warning_logger.warning(f'Task {sender} is retrying to be executed for this reason {reason}')


# logs for when a task fails due to internal error
@task_internal_error.connect
def log_when_task_is_retrying(sender=None, exception=None, task_id=None, **kwargs):
    tasks_critical_logger.critical(
        f'Task {sender} with task id {task_id} failed due to this internal error: str({exception})')


# ----------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------Worker Logs----------------------------------------------------------
from celery.signals import worker_init, worker_ready, worker_shutdown, worker_shutting_down, worker_process_shutdown, \
    worker_process_init
from utils.logging.loggers import worker_logger


#  log for when a worker instance is initialized
@worker_init.connect
def log_when_worker_starts(sender=None, **kwargs):
    worker_logger.info(f'Worker with hostname: {sender.hostname} has started')


#  log when a worker is ready to execute tasks
@worker_ready.connect
def log_when_worker_ready(sender=None, **kwargs):
    worker_logger.info(f'Worker with hostname: {sender} is ready to receive tasks')


#  log when a worker is shutting down
@worker_shutting_down.connect
def log_when_worker_is_shutting_down(sender=None, **kwargs):
    worker_logger.info(f'Worker with hostname: {sender} is shutting down')


#  log when a worker has shutdown
@worker_shutdown.connect
def log_when_worker_shutdown(sender=None, **kwargs):
    worker_logger.info(f'Worker with hostname: {sender} has shutdown')


#  log when a worker process is initializing
@worker_process_init.connect
def log_when_worker_process_initialize(sender=None, **kwargs):
    worker_logger.info(f'Worker process with hostname: {sender} is initializing')


#  log when a worker process is initializing
@worker_process_shutdown.connect
def log_when_worker_process_shutdown(sender=None, **kwargs):
    worker_logger.info(f'Worker process with hostname: {sender} has shutdown')