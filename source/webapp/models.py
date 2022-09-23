from django.db import models


class TasksList(models.Model):
    choices = [('new', 'Новая'), ('in_process', 'В процессе'), ('done', 'Сделано')]

    title = models.TextField(max_length=1000, null=False, blank=False, default='None', verbose_name='Задача')
    status = models.CharField(max_length=200, choices=choices, default='new', verbose_name='Статус')
    deadline = models.DateField(null=True, blank=True, verbose_name='Срок выполнения')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.title} - {self.status} - {self.deadline}"
