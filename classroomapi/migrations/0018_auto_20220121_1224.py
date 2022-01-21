# Generated by Django 3.2.10 on 2022-01-21 12:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classroomapi', '0017_organisation_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True)),
                ('emoji', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('TXT', 'Text'), ('IMG', 'Image')], default='TXT', max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='clip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clip',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='link',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subtitle',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subtitle',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='HighlightRect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.FloatField()),
                ('y1', models.FloatField()),
                ('x2', models.FloatField()),
                ('y2', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('page_number', models.IntegerField(blank=True, default=0)),
                ('parent_rect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroomapi.highlight')),
            ],
        ),
        migrations.AddField(
            model_name='highlight',
            name='bounding_rect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroomapi.highlightrect'),
        ),
        migrations.AddField(
            model_name='highlight',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroomapi.course'),
        ),
        migrations.AddField(
            model_name='highlight',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroomapi.resource'),
        ),
    ]
