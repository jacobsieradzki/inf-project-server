# Generated by Django 3.2.9 on 2021-11-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroomapi', '0004_event_meeting_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
