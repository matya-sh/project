# Generated by Django 3.1 on 2022-01-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_artiles_pikcha'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiles',
            name='img',
            field=models.ImageField(default=1, height_field=100, upload_to='', verbose_name='Картинка', width_field=100),
            preserve_default=False,
        ),
    ]
