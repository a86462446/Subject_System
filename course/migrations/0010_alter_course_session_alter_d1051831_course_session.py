# Generated by Django 4.1.7 on 2023-10-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_session_d1051831_course_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='session',
            field=models.CharField(max_length=10, null=True, verbose_name='節次'),
        ),
        migrations.AlterField(
            model_name='d1051831_course',
            name='session',
            field=models.CharField(max_length=10, null=True, verbose_name='節次'),
        ),
    ]
