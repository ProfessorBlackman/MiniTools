# Generated by Django 4.2.2 on 2023-08-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BitLink', '0002_remove_urldata_timestamp_urldata_expires_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='urldata',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
