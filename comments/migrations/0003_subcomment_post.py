# Generated by Django 3.2.3 on 2021-05-25 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_new_date_created'),
        ('comments', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcomment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.new'),
            preserve_default=False,
        ),
    ]
