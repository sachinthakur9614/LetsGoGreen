# Generated by Django 2.1 on 2019-07-16 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TreePlant', '0004_treegwothapproval'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TreeGwothApproval',
            new_name='TreeGrowthApproval',
        ),
        migrations.AlterField(
            model_name='treegrowthapproval',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TreePlant.TreeGrowth'),
        ),
    ]
