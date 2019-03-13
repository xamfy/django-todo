from django.core.management import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
import datetime
from main.models import Schedule


class Command(BaseCommand):
    def handle(self, **options):
        today = datetime.datetime.now().date()
        # today = datetime.date.today()
        # print(datetime.datetime.now().date())
        for schedule in Schedule.objects.filter(date=today, completed=False):
            print(schedule.user.email)
            subject = 'Schedule reminder'
            body = 'Hey, please complete your schedule ' + schedule.name
            send_mail(subject, body, 'contact@example.com',
                      [schedule.user.email])
