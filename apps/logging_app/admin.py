from django.contrib import admin

from apps.logging_app.models.user_logs_model import UserLogsEntryModel


class LoggingAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'level', 'module', 'funcName', 'line_num', 'message')


# Register your models here.
admin.site.register(UserLogsEntryModel)
