# Generated by Django 4.1.9 on 2023-12-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_address_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, choices=[('UK', 'United Kingdom'), ('US', 'United States'), ('FR', 'France'), ('GER', 'Germany')], max_length=300),
        ),
    ]