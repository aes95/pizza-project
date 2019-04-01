# Generated by Django 2.0.3 on 2019-03-25 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20190313_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='food',
        ),
        migrations.AddField(
            model_name='orderline',
            name='food',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Food'),
            preserve_default=False,
        ),
    ]