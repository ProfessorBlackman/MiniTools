# Generated by Django 4.2.2 on 2023-07-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogsEntryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(max_length=20)),
                ('funcName', models.CharField()),
                ('line_num', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
