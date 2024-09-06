# Generated by Django 4.2.2 on 2023-06-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_transaksi_token_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='status',
            field=models.CharField(blank=True, choices=[('Belum Lunas', 'Belum Lunas'), ('Lunas', 'Lunas'), ('Pengiriman', 'Pengiriman'), ('Selesai', 'Selesai'), ('Batalkan', 'Batalkan'), ('Kadaluarsa', 'Kadaluarsa'), ('Pembayaran Ditolak', 'Pembayaran Ditolak')], default='Belum Lunas', max_length=200, null=True),
        ),
    ]