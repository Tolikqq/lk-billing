# Generated by Django 3.0.2 on 2020-01-28 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='subject',
        ),
        migrations.AddField(
            model_name='feedback',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.CharField(max_length=5000, verbose_name='Сообщение'),
        ),
    ]
