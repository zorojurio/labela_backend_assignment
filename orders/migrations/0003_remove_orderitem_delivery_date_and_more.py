# Generated by Django 4.0.3 on 2023-09-17 12:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_id_remove_order_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='line_item_cost',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='line_item_total_cost',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 12, 59, 27, 679510, tzinfo=utc)),
            preserve_default=False,
        ),
    ]