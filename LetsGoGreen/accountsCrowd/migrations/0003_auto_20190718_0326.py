# Generated by Django 2.1 on 2019-07-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsCrowd', '0002_auto_20190717_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowduserprofile',
            name='address',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='crowduserprofile',
            name='phone',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='crowduserprofile',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='crowduserprofile',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
