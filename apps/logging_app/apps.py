from django.apps import AppConfig

from project.settings import log_files
from utils.logging.custom_logging import DetailedJsonFormatter, DefaultJsonFormatter


class LoggingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.logging_app'
    handle = "logging.FileHandler"

    def ready(self):
        from apps.logging_app.services.database_handler import DatabaseHandler
        import logging.config

        logging.config.dictConfig({
            "version": 1,
            "disable_existing_loggers": False,
            # "root": {
            #     "handlers": ["console", "MiniTools"],
            #     "level": "DEBUG",
            # },
            "formatters": {
                "simple": {
                    "format": "{levelname}: {message}",
                    "style": "{",
                },
                "default": {
                    "format": "[{asctime}] {levelname} {name}: {message}",
                    "style": "{",
                },
                "default_json_formatter": {"()": DefaultJsonFormatter},
                "detailed": {
                    "format": "[{asctime}] {levelname} {module} {funcName} {lineno} {message}",
                    "style": "{",
                },
                "detailed_json_formatter": {"()": DetailedJsonFormatter},
            },
            "filters": {
                "require_debug_false": {
                    "()": "django.utils.log.RequireDebugFalse",
                }
            },
            "handlers": {
                "console": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                },
                "database_log": {
                    'level': 'DEBUG',
                    'class': 'apps.logging_app.services.database_handler.DatabaseHandler',
                    'formatter': 'default_json_formatter',
                },
                "mail_admins": {
                    'level': 'ERROR',
                    "filters": ["require_debug_false"],
                    'class': 'django.utils.log.AdminEmailHandler',
                    'include_html': True,
                },
                "tasks_info": {
                    "level": "DEBUG",
                    "class": self.handle,
                    "filename": log_files["tasks_info_log"],
                    "formatter": "default_json_formatter",
                },
                "tasks_errors": {
                    "level": "ERROR",
                    "class": self.handle,
                    "filename": log_files["tasks_errors_log"],
                    "formatter": "default_json_formatter",
                },
                "tasks_critical": {
                    "level": "CRITICAL",
                    "class": self.handle,
                    "filename": log_files["tasks_critical_log"],
                    "formatter": "default_json_formatter",
                },
                "tasks_warnings": {
                    "level": "WARNING",
                    "class": self.handle,
                    "filename": log_files["tasks_warnings_log"],
                    "formatter": "default_json_formatter",
                },
                "worker_info": {
                    "level": "INFO",
                    "class": self.handle,
                    "filename": log_files["worker_info_log"],
                    "formatter": "default_json_formatter",
                },
                "MiniTools": {
                    "level": "INFO",
                    "class": self.handle,
                    "filename": log_files["mini"],
                    "formatter": "default_json_formatter",
                },
                "database": {
                    "level": "DEBUG",
                    "class": self.handle,
                    "filename": log_files["database"],
                    "formatter": "default_json_formatter",
                },
            },
            "loggers": {
                "tasks_info": {"handlers": ["console", "tasks_info"]},
                "tasks_error": {"handlers": ["console", "tasks_errors"]},
                "tasks_warning": {"handlers": ["console", "tasks_warnings"]},
                "tasks_critical": {"handlers": ["console", "tasks_critical"]},
                "worker": {"handlers": ["console", "worker_info"]},
                "minitools": {"handlers": ["console", "MiniTools"]},
                "db_logger": {"handlers": ["console", "database"]},
                "db_entry": {"handlers": ["database_log"], 'level': 'DEBUG', 'propagate': True, },
            },

        })
