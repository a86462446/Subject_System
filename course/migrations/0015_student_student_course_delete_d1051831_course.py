# Generated by Django 4.1.7 on 2023-10-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_alter_course_code_alter_d1051831_course_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='', max_length=10, verbose_name='學生名稱')),
                ('student_number', models.CharField(default='', max_length=15, verbose_name='學號')),
                ('student_class', models.CharField(default='', max_length=15, verbose_name='系級')),
                ('student_password', models.CharField(default='', max_length=16, verbose_name='密碼')),
            ],
        ),
        migrations.CreateModel(
            name='Student_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(default='', max_length=15, verbose_name='學號')),
                ('name', models.CharField(max_length=20, verbose_name='科目名稱')),
                ('code', models.CharField(max_length=10, verbose_name='選課代碼')),
                ('classs', models.CharField(max_length=20, verbose_name='開課班級')),
                ('required_elective', models.CharField(max_length=20, verbose_name='必選修')),
                ('credit', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='學分')),
                ('time', models.CharField(max_length=25, verbose_name='課程時間')),
                ('start_session', models.IntegerField(null=True, verbose_name='開始節次')),
                ('end_session', models.IntegerField(null=True, verbose_name='結束節次')),
                ('week', models.CharField(max_length=3, null=True, verbose_name='星期')),
            ],
        ),
        migrations.DeleteModel(
            name='D1051831_course',
        ),
    ]