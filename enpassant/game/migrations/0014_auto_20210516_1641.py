# Generated by Django 3.2 on 2021-05-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_auto_20210515_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='last_fen',
        ),
        migrations.AddField(
            model_name='game',
            name='pgn',
            field=models.TextField(default=''),
        ),
    ]