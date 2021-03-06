# Generated by Django 2.2.5 on 2019-10-15 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MahjongRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_url', models.URLField(blank=True)),
                ('player_name', models.CharField(max_length=16)),
                ('creat_date', models.DateTimeField(default=datetime.datetime.now)),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
    ]
