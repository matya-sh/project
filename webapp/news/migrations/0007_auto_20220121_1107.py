# Generated by Django 3.1 on 2022-01-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20220121_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles',
            name='img',
            field=models.ImageField(upload_to='media/news/', verbose_name='Картинка'),
        ),
    ]
