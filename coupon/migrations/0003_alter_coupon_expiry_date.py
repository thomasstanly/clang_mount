# Generated by Django 4.2.7 on 2023-12-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_alter_coupon_coupon_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='expiry_date',
            field=models.DateField(blank=True),
        ),
    ]
