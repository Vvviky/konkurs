# Generated by Django 3.1.7 on 2021-06-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_galeryphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='galeryphoto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
