# Generated by Django 4.1.9 on 2023-12-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('end_point', '0016_alter_laptop_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='price',
            field=models.FloatField(max_length=100, null=True),
        ),
    ]
