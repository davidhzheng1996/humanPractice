# Generated by Django 2.1.5 on 2019-05-08 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopword', models.BooleanField(default=False)),
                ('data', models.TextField(default='')),
                ('timestamp', models.TextField(default='')),
                ('text', models.TextField(default='')),
            ],
        ),
    ]
