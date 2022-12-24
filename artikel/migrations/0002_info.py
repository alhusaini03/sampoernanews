# Generated by Django 4.1.4 on 2022-12-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=1000)),
                ('categoris', models.CharField(max_length=1000)),
                ('isodate', models.DateTimeField()),
                ('description', models.TextField()),
                ('image', models.ImageField(max_length=1000, upload_to='')),
            ],
        ),
    ]
