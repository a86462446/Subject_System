# Generated by Django 4.1.7 on 2023-10-20 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_student_student_course_delete_d1051831_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_password',
        ),
    ]
