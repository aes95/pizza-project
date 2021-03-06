# Generated by Django 2.0.3 on 2019-02-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_dinnerplatter_pasta_salad_steakandcheese_sub'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sub',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='sub',
            unique_together={('name', 'large', 'extra_cheese')},
        ),
    ]
