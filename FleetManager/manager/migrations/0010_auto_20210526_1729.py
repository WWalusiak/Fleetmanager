# Generated by Django 3.1.7 on 2021-05-26 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20210526_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='companyID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='manager.company'),
        ),
    ]
