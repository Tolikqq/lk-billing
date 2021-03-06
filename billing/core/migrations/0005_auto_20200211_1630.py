# Generated by Django 3.0.2 on 2020-02-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_order_countuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=18, verbose_name='Сумма'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='countuser',
            field=models.IntegerField(verbose_name='Количество пользователей'),
        ),
    ]
