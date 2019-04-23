from django.db import models
from django.conf import settings
from src.models.room.models import Room


class Message(models.Model):
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text            = models.TextField(blank=False)
    room            = models.ForeignKey(Room, on_delete=models.CASCADE)
    create_date     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']


    def __str__(self):
        return f"{self.text}"
