# Generated by Django 3.2.12 on 2023-07-12 22:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0004_coupon_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 22, 12, 18, 694869, tzinfo=utc)),
        ),
    ]
