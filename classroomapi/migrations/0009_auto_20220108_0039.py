# Generated by Django 3.2.9 on 2022-01-08 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroomapi', '0008_auto_20211209_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_link_id', models.CharField(max_length=20)),
                ('min_link_type', models.CharField(choices=[('EVENT', 'Event'), ('MEETING', 'Meeting'), ('RESOURCE', 'Resource'), ('CLIP', 'Clip'), ('LOCATION', 'Location'), ('COMMENT', 'Comment')], max_length=16)),
                ('max_link_id', models.CharField(max_length=20)),
                ('max_link_type', models.CharField(choices=[('EVENT', 'Event'), ('MEETING', 'Meeting'), ('RESOURCE', 'Resource'), ('CLIP', 'Clip'), ('LOCATION', 'Location'), ('COMMENT', 'Comment')], max_length=16)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroomapi.course')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.CharField(blank=True, default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(blank=True, default='', max_length=60),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Meeting',
        ),
    ]
