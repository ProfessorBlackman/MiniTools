import logging


default_logger = logging.getLogger(__name__)
tasks_logger = logging.getLogger("tasks_info")
tasks_error_logger = logging.getLogger("tasks_error")
tasks_warning_logger = logging.getLogger("tasks_warning")
tasks_critical_logger = logging.getLogger("tasks_critical")
worker_logger = logging.getLogger("worker")
redis_logger = logging.getLogger("redis_logger")
db_logger = logging.getLogger("db_logger")
mini = logging.getLogger("minitools")
database_logger = logging.getLogger("db_entry")
