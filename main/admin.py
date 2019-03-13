from django.contrib import admin
from .models import Schedule


# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('schedule', 'name', 'time', 'completed')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'date', 'completed')


admin.site.register(Schedule, ScheduleAdmin)
# admin.site.register(Task, TaskAdmin)
