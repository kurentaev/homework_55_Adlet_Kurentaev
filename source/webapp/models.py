from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    NEW = 'new', 'New'
    IN_PROCESS = 'in_process', 'In process'
    DONE = 'done', 'Done'


class TasksList(models.Model):
    title = models.TextField(max_length=200, null=False, blank=False, verbose_name='Задача')
    status = models.CharField(verbose_name='Статус', choices=StatusChoices.choices, max_length=100,
                              default=StatusChoices.NEW)
    deadline = models.DateField(null=True, blank=True, verbose_name='Срок выполнения')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.title} - {self.status} - {self.deadline}"
