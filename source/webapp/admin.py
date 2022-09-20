from django.contrib import admin

from webapp.models import TasksList


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'deadline']
    list_filter = ['id', 'description', 'status', 'deadline']
    search_fields = ['description', 'status']
    fields = ['id', 'description', 'status', 'deadline']
    readonly_fields = ['id', 'deadline']


admin.site.register(TasksList, TaskAdmin)

