# Generated by Django 2.0.3 on 2019-02-11 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_pizza_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatter',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('large', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='SteakAndCheese',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('large', models.BooleanField(default=False)),
                ('cheese', models.BooleanField(default=False)),
                ('mushrooms', models.BooleanField(default=False)),
                ('peppers', models.BooleanField(default=False)),
                ('onions', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('large', models.BooleanField(default=False)),
                ('extra_cheese', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
    ]
