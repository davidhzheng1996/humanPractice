# Generated by Django 2.1.5 on 2019-05-19 21:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190519_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='words',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=''), size=25), size=1),
        ),
    ]