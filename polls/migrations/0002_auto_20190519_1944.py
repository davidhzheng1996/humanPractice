# Generated by Django 2.1.5 on 2019-05-19 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysis',
            old_name='data',
            new_name='words',
        ),
    ]
