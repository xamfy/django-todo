from django.db import models
import datetime


class Schedule(models.Model):
    user = models.ForeignKey(
        'auth.User', related_name='schedules', on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=50, default=datetime.date.today)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# class Task(models.Model):
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     time = models.TimeField()
#     completed = models.BooleanField(default=False)

#     class Meta:
#         ordering = ('time',)

#     def __str__(self):
#         return self.name
