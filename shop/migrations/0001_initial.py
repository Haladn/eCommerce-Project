# Generated by Django 4.1.9 on 2023-11-28 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('end_point', '0015_alter_laptop_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, choices=[('UK', 'United Kingdom'), ('US', 'United States'), ('FR', 'France'), ('GER', 'Germany')], max_length=300)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('building_name', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(max_length=300, null=True)),
                ('postal_code', models.CharField(max_length=300, null=True)),
                ('formatted_address', models.CharField(blank=True, max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ctreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='img.png', null=True, upload_to='images/')),
                ('country_code', models.CharField(choices=[('UK', 'UK +44'), ('US', 'US +1'), ('FR', 'FR +33'), ('GER', 'GER +49')], max_length=11)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FormattedAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formatted_address', models.CharField(blank=True, max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.address')),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0.0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('pendding', 'pendding'), ('on way to delivery', 'on way to delivery'), ('delivered', 'delivered')], default='pendding', max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
                ('formatted_adddress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.formattedaddress')),
                ('laptop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='end_point.laptop')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
                ('laptop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='end_point.laptop')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.customer'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.customer'),
        ),
    ]
