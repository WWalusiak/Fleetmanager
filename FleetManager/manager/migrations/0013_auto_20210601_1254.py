# Generated by Django 3.1.7 on 2021-06-01 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20210601_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='costs_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='exploitation_cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='final_mileage',
            field=models.IntegerField(null=True),
        ),
    ]
