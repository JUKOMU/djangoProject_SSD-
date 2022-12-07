# Generated by Django 4.1.1 on 2022-12-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=40)),
                ('lesson_hour', models.CharField(max_length=30)),
                ('lesson_week', models.CharField(max_length=40)),
                ('lesson_date', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('teacher', models.CharField(max_length=30)),
                ('classroom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (0, 'Female')])),
                ('department', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('class_i', models.IntegerField()),
                ('party_member', models.IntegerField(choices=[(1, 'is'), (0, 'not')])),
                ('selected_lessons', models.CharField(max_length=100)),
            ],
        ),
    ]
