# Generated by Django 3.1.3 on 2020-11-19 19:06

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
                ('header', models.CharField(max_length=56, verbose_name='header')),
                ('text', models.CharField(max_length=256, verbose_name='text')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='datetime')),
                ('is_read', models.BooleanField(default=False, verbose_name='is it already read?')),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
            },
        ),
    ]
