# Generated by Django 4.1.9 on 2023-12-15 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('end_point', '0019_alter_laptop_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='href',
        ),
    ]
