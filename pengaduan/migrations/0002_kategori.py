# Generated by Django 3.0 on 2020-06-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengaduan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=100)),
                ('deskripsi', models.CharField(max_length=500)),
            ],
        ),
    ]
