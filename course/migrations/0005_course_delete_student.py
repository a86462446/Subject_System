# Generated by Django 4.1.7 on 2023-10-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='科目名稱')),
                ('code', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='選課代碼')),
                ('classs', models.CharField(max_length=20, verbose_name='開課班級')),
                ('required_elective', models.CharField(max_length=20, verbose_name='必選修')),
                ('credit', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='學分')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
