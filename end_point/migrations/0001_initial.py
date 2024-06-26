# Generated by Django 4.2.2 on 2023-06-28 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('img_link', models.CharField(max_length=500)),
                ('href', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
