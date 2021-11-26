# Generated by Django 3.2.9 on 2021-11-26 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroomapi', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('type', models.CharField(choices=[('VID', 'Video'), ('YT', 'YouTube'), ('PDF', 'PDF'), ('URL', 'URL'), ('IMG', 'IMG')], default='URL', max_length=16)),
                ('url', models.URLField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroomapi.course')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('url', models.URLField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroomapi.course')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('type', models.CharField(choices=[('LECTURE', 'Lecture'), ('WORKSHOP', 'Workshop'), ('ASSIGNMENT', 'Assignment')], default='LECTURE', max_length=16)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroomapi.course')),
            ],
        ),
    ]
