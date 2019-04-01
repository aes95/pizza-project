# Generated by Django 2.0.3 on 2019-03-12 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0011_auto_20190306_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('type', models.CharField(max_length=32)),
                ('sub_type', models.CharField(blank=True, max_length=32)),
                ('size', models.CharField(blank=True, choices=[('S', 'Small'), ('L', 'Large')], max_length=1)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4)),
                ('add_on', models.ManyToManyField(blank=True, to='orders.AddOns')),
                ('toppings', models.ManyToManyField(blank=True, to='orders.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=99)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('food', models.ManyToManyField(blank=True, to='orders.Food')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]
