# Generated by Django 4.1.1 on 2022-09-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_taskslist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskslist',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in_process', 'In process'), ('done', 'Done')], default='new', max_length=100, verbose_name='Статус'),
        ),
    ]
