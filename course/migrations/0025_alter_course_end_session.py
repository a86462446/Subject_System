# Generated by Django 4.1.7 on 2023-11-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_alter_student_course_end_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_session',
            field=models.IntegerField(verbose_name='結束節次'),
        ),
    ]
