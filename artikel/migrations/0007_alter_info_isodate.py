# Generated by Django 4.1.4 on 2022-12-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0006_info_author_info_content_alter_info_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='isodate',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
