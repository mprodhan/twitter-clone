# Generated by Django 3.0.6 on 2020-06-01 01:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_tweet_twitteruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
