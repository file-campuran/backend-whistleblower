# Generated by Django 3.0 on 2020-06-07 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pengaduan', '0003_auto_20200607_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aduan',
            old_name='deskripsi',
            new_name='deskripsi_aduan',
        ),
    ]
