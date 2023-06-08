import logging


default_logger = logging.getLogger(__name__)
tasks_logger = logging.getLogger("log_tasks_info")
tasks_error_logger = logging.getLogger("log_tasks_error")
tasks_warning_logger = logging.getLogger("log_tasks_warning")
tasks_critical_logger = logging.getLogger("log_tasks_critical")
worker_logger = logging.getLogger("log_worker")
redis_logger = logging.getLogger("redis_logger")
db_logger = logging.getLogger("db_logger")