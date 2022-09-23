from django.contrib import admin

from webapp.models import TasksList


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'deadline', 'description']
    list_filter = ['id', 'title', 'status', 'deadline', 'description']
    search_fields = ['title', 'status']
    fields = ['id', 'title', 'status', 'deadline', 'description']
    readonly_fields = ['id']


admin.site.register(TasksList, TaskAdmin)

