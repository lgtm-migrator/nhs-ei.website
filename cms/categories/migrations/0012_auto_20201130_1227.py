# Generated by Django 3.1.3 on 2020-11-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0011_auto_20201130_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='wp_id',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
