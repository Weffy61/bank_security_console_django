from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self, enter_time, leave_time=localtime()):
        sec_delta = int((leave_time - enter_time).total_seconds())
        return sec_delta

    def format_duration(self, seconds):
        hours = (seconds // 60) // 60
        minutes = (seconds // 60) % 60
        seconds = (seconds % 60)
        duration = {'hours': hours,
                    'minutes': minutes,
                    'seconds': seconds}
        return f'{duration["hours"]:02d}:{duration["minutes"]:02d}:{duration["seconds"]:02d}'

    def is_visit_long(self, visit, minutes=60):
        return visit > minutes * 60
