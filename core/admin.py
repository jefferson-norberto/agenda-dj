from django.contrib import admin
from core.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'event_date', 'create_date')
    list_filter = (['user'])

# Register your models here.
admin.site.register(Event, EventAdmin)