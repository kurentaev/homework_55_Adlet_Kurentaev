# Generated by Django 4.1.1 on 2022-09-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskslist',
            name='title',
            field=models.TextField(default='None', max_length=1000, verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='taskslist',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание'),
        ),
    ]