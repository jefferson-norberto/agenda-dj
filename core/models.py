from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now=True)
    local = models.CharField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    
    def __str__(self) -> str:
        return self.title

    def get_event_date(self):
        return self.event_date.strftime('%d/%m/%Y -> %H:%M Hrs')
    
    def get_date_input_event(self):
        return self.event_date.strftime('%Y-%m-%dT%H:%M')

    def get_later_event(self):
        if self.event_date < datetime.now():
            return True
        return False
