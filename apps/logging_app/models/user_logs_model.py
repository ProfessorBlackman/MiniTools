from django.db import models


class UserLogsEntryModel(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=20)
    module = models.CharField()
    funcName = models.CharField()
    line_num = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.module} - {self.funcName}"
