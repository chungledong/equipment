# Generated by Django 4.0.2 on 2022-03-01 14:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0003_alter_units_options_alter_units_active_and_more'),
        ('supplies', '0002_alter_groupsupplies_name_alter_supplies_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupsupplies',
            options={'verbose_name_plural': 'Nhóm vật tư'},
        ),
        migrations.AlterModelOptions(
            name='supplies',
            options={'verbose_name_plural': 'Vật tư'},
        ),
        migrations.AlterField(
            model_name='groupsupplies',
            name='description',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Mô tả nhóm vật tư'),
        ),
        migrations.AlterField(
            model_name='supplies',
            name='description',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Mô tả vật tư'),
        ),
        migrations.AlterField(
            model_name='supplies',
            name='group_supplies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplies.groupsupplies', verbose_name='Nhóm vật tư'),
        ),
        migrations.AlterField(
            model_name='supplies',
            name='image',
            field=models.ImageField(default='No_image.png', upload_to='device/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='supplies',
            name='units',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='units.units', verbose_name='Đơn vị tính'),
        ),
    ]
