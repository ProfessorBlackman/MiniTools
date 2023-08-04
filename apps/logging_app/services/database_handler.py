import logging

from apps.logging_app.models.user_logs_model import UserLogsEntryModel


class DatabaseHandler(logging.Handler):
    def emit(self, record):
        print(f"this is form: {record.getMessage()}")
        log_entry = UserLogsEntryModel(
            level=record.levelname,
            message=record.getMessage(),
            module=record.module,
            funcName=record.funcName,
            line_num=record.lineno
        )
        log_entry.save()
