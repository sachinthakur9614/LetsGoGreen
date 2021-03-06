# Generated by Django 2.1 on 2019-07-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sapling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treeName', models.CharField(max_length=100)),
                ('treeDescription', models.TextField(max_length=1000)),
                ('treeImage', models.ImageField(upload_to='images/')),
                ('leaf', models.CharField(max_length=100)),
                ('life', models.IntegerField()),
                ('root', models.CharField(max_length=100)),
                ('stem', models.CharField(max_length=100)),
                ('shoot', models.CharField(max_length=100)),
            ],
        ),
    ]
