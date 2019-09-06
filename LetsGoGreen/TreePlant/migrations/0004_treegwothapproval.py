# Generated by Django 2.1 on 2019-07-16 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TreePlant', '0003_auto_20190716_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeGwothApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprroveTree', models.BooleanField(blank=True)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TreePlant.TreeType')),
                ('us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
