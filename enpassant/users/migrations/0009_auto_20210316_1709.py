# Generated by Django 3.1.7 on 2021-03-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210315_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]
