# Generated by Django 4.1.7 on 2023-10-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_course_week_d1051831_course_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_session',
            field=models.IntegerField(null=True, verbose_name='結束節次'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_session',
            field=models.IntegerField(null=True, verbose_name='開始節次'),
        ),
        migrations.AlterField(
            model_name='d1051831_course',
            name='end_session',
            field=models.IntegerField(null=True, verbose_name='結束節次'),
        ),
        migrations.AlterField(
            model_name='d1051831_course',
            name='start_session',
            field=models.IntegerField(null=True, verbose_name='開始節次'),
        ),
    ]
