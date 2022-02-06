# Generated by Django 3.2.10 on 2022-02-06 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroomapi', '0022_auto_20220206_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='membership',
        ),
        migrations.AddField(
            model_name='membership',
            name='organisation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='classroomapi.organisation'),
            preserve_default=False,
        ),
    ]