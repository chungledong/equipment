# Generated by Django 4.0.2 on 2022-02-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.TextField(verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='groupdevice',
            name='name',
            field=models.TextField(verbose_name='name'),
        ),
    ]
