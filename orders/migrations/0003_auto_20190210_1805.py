# Generated by Django 2.0.3 on 2019-02-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190210_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sicilian', models.BooleanField(default=False)),
                ('large', models.BooleanField(default=False)),
                ('toppings_count', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=2)),
            ],
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]