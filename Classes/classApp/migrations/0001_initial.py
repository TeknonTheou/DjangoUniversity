# Generated by Django 4.0.4 on 2022-04-22 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, default='', max_length=60)),
                ('Course_Number', models.IntegerField(blank=True, default=0)),
                ('Instructor_Name', models.CharField(blank=True, default='', max_length=60)),
                ('Duration', models.FloatField(default=0.0)),
            ],
        ),
    ]
