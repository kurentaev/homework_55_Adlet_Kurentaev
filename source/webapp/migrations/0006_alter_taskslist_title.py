# Generated by Django 4.1.1 on 2022-09-30 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_taskslist_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskslist',
            name='title',
            field=models.TextField(max_length=200, verbose_name='Задача'),
        ),
    ]
