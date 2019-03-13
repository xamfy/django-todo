# django-todo

We can run a cron job to send email to user's email when the date set on the schedule is equal to today.
It will run the schedule_reminder management command which will send the emails using mailgun.

Example: 
```
0 0 * * * cd /home/xamfy/django/todo-app; /home/xamfy/django/todo-app/venv/bin/python manage.py schedule_reminder
```
