# Generated by Django 3.1.5 on 2021-01-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210117_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='plants',
            field=models.ManyToManyField(through='core.OrderPlant', to='core.Plant'),
        ),
    ]
