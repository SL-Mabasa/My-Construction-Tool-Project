# Generated by Django 5.1.6 on 2025-03-10 05:49

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_prices_delete_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='prices',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='prices',
            name='description',
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('phone', models.CharField(blank=True, default='', max_length=10)),
                ('status', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='prices',
        ),
    ]
