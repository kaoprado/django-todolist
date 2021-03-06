# Generated by Django 2.1.5 on 2019-01-08 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True)),
                ('created_at', models.DateField(blank=True, default=datetime.datetime.now)),
                ('completed', models.IntegerField(default=0, max_length=1)),
            ],
        ),
    ]
