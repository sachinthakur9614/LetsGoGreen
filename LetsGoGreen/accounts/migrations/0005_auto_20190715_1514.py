# Generated by Django 2.1 on 2019-07-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190715_0104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='amountDonated',
            new_name='amountRecieve',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='review',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='follower',
            field=models.IntegerField(blank=True, default=100.1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rank',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='totalTree',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
