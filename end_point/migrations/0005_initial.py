# Generated by Django 4.1.9 on 2023-09-05 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('end_point', '0004_delete_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.CharField(max_length=500)),
                ('href', models.CharField(max_length=1000)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(choices=[('electronics', 'electronics')], default='electronics', max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]