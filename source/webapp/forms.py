from django import forms
from django.core.exceptions import ValidationError

from webapp.models import TasksList


class TasksListForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data.get('title')
        print(title)
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее двух символов')
        return title

    class Meta:
        model = TasksList
        fields = ('title', 'status', 'deadline', 'description')
