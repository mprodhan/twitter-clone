# Generated by Django 3.0.6 on 2020-06-05 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_auto_20200601_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.TextField(max_length=140),
        ),
    ]
