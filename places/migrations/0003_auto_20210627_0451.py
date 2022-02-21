# Generated by Django 3.1.7 on 2021-06-27 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20210626_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='place',
            name='image_1',
            field=models.ImageField(upload_to='place/', verbose_name='Изображение 1'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image_2',
            field=models.ImageField(upload_to='place/', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image_3',
            field=models.ImageField(upload_to='place/', verbose_name='Изображение 3'),
        ),
        migrations.AlterField(
            model_name='place',
            name='is_pamyatnik',
            field=models.BooleanField(default=False, verbose_name='Это памятник ?'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название места'),
        ),
        migrations.AlterField(
            model_name='place',
            name='text_1',
            field=models.TextField(verbose_name='Текст описания 1'),
        ),
        migrations.AlterField(
            model_name='place',
            name='text_2',
            field=models.TextField(verbose_name='Текст описания 2'),
        ),
        migrations.AlterField(
            model_name='place',
            name='text_3',
            field=models.TextField(verbose_name='Текст описания 3'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Краткое описание'),
        ),
    ]
