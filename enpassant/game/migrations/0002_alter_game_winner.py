# Generated by Django 3.2 on 2021-05-07 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
    ]
