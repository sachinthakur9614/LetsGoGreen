# Generated by Django 2.1 on 2019-07-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreePlant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treeName', models.CharField(max_length=100)),
                ('treeImage', models.ImageField(upload_to='images/')),
                ('treeDescription', models.TextField(max_length=1000)),
                ('lifeTime', models.IntegerField()),
            ],
        ),
    ]