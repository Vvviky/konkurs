# Generated by Django 3.1.7 on 2021-06-27 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20210626_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='galeryphoto',
            options={'verbose_name': 'Фотография из галереи', 'verbose_name_plural': 'Фотографии из галереи'},
        ),
        migrations.AlterField(
            model_name='about',
            name='about_image',
            field=models.ImageField(upload_to='about/', verbose_name='Изображение библиотеки'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_1',
            field=models.ImageField(upload_to='about/', verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_2',
            field=models.ImageField(upload_to='about/', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_3',
            field=models.ImageField(upload_to='about', verbose_name='Изображение 3'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_4',
            field=models.ImageField(upload_to='about/', verbose_name='Изображение 4'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_5',
            field=models.ImageField(upload_to='about/', verbose_name='Изображение 5'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_6',
            field=models.ImageField(upload_to='about/', verbose_name='Изображение 6'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_7',
            field=models.ImageField(upload_to='about/', verbose_name='Изображение 7'),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_8',
            field=models.ImageField(upload_to='about/', verbose_name='Изображение 8'),
        ),
        migrations.AlterField(
            model_name='about',
            name='text_1',
            field=models.TextField(verbose_name='История библиотеки 1'),
        ),
        migrations.AlterField(
            model_name='about',
            name='text_2',
            field=models.TextField(verbose_name='История библиотеки 2'),
        ),
        migrations.AlterField(
            model_name='about',
            name='text_3',
            field=models.TextField(verbose_name='История библиотеки 3'),
        ),
        migrations.AlterField(
            model_name='about',
            name='text_about',
            field=models.TextField(verbose_name='Дополнительный текст'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title_about',
            field=models.TextField(verbose_name='Основной текст'),
        ),
        migrations.AlterField(
            model_name='galeryphoto',
            name='image',
            field=models.ImageField(upload_to='galery/', verbose_name='Изображение'),
        ),
    ]