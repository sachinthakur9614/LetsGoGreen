# Generated by Django 2.1 on 2019-07-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreePlant', '0007_auto_20190716_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='treelocation',
            name='pincode',
            field=models.BigIntegerField(default=21122),
            preserve_default=False,
        ),
    ]
