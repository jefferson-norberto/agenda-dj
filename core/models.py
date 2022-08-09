from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    
    def __str__(self) -> str:
        return self.title