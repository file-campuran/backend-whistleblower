# Generated by Django 3.0 on 2020-06-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengaduan', '0006_aduan_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='aduan',
            name='status_aduan',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
