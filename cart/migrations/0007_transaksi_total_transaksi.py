# Generated by Django 4.2.2 on 2023-06-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_transaksi_custumer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaksi',
            name='total_transaksi',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]