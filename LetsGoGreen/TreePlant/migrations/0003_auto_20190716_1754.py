# Generated by Django 2.1 on 2019-07-16 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TreePlant', '0002_treecatalog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treegrowth',
            name='tree',
        ),
        migrations.AddField(
            model_name='treegrowth',
            name='us',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
