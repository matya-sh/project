# Generated by Django 3.1 on 2022-01-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220120_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles',
            name='pikcha',
            field=models.BinaryField(verbose_name='Картинка'),
        ),
    ]
