# Generated by Django 4.1.1 on 2022-09-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TasksList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='None', max_length=3000, verbose_name='Описание')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_process', 'В процессе'), ('done', 'Сделано')], default='new', max_length=200, verbose_name='Статус')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Срок выполнения')),
            ],
        ),
    ]
