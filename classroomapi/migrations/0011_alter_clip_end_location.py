# Generated by Django 3.2.9 on 2022-01-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroomapi', '0010_auto_20220108_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clip',
            name='end_location',
            field=models.IntegerField(null=True),
        ),
    ]
