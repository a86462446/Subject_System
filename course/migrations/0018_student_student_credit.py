# Generated by Django 4.1.7 on 2023-10-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_alter_student_course_student_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_credit',
            field=models.IntegerField(default=0, verbose_name='學分'),
        ),
    ]
