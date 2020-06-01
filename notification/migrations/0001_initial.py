# Generated by Django 3.0.6 on 2020-05-31 23:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_post', models.DateTimeField(default=django.utils.timezone.now)),
                ('message_visibility', models.BooleanField(default=True)),
            ],
        ),
    ]
