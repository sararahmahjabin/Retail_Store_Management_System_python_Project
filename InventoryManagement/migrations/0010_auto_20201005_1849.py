# Generated by Django 3.0.8 on 2020-10-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagement', '0009_auto_20201005_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(default='N\\A', max_length=200),
        ),
    ]