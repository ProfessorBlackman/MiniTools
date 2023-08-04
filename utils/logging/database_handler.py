import logging

from apps.logging_app.models.user_logs_model import UserLogsEntryModel


class DatabaseHandler(logging.Handler):
    def emit(self, record):
        log_entry = UserLogsEntryModel(
            level=record.levelname,
            message=self.format(record),
            module=record.module,
            funcName=record.funcName,
            line_num=record.lineno,
            timestamp=record.asctime
        )
        log_entry.save()
