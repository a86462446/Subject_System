# Generated by Django 4.1.7 on 2023-10-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_student_student_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credit',
            field=models.IntegerField(verbose_name='學分'),
        ),
    ]
