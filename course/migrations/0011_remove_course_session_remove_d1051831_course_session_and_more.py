# Generated by Django 4.1.7 on 2023-10-17 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_alter_course_session_alter_d1051831_course_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='session',
        ),
        migrations.RemoveField(
            model_name='d1051831_course',
            name='session',
        ),
        migrations.AddField(
            model_name='course',
            name='end_session',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='結束節次'),
        ),
        migrations.AddField(
            model_name='course',
            name='start_session',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='開始節次'),
        ),
        migrations.AddField(
            model_name='d1051831_course',
            name='end_session',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='結束節次'),
        ),
        migrations.AddField(
            model_name='d1051831_course',
            name='start_session',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='開始節次'),
        ),
    ]
