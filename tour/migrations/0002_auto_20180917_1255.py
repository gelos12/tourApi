# Generated by Django 2.1.1 on 2018-09-17 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewstar',
            name='td',
        ),
        migrations.RemoveField(
            model_name='reviewstar',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='stars',
        ),
        migrations.DeleteModel(
            name='ReViewStar',
        ),
    ]
