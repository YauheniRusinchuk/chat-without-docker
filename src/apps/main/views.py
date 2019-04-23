from django.views.generic.list import ListView
from src.models.room.models import Room


class ListRoom(ListView):

    queryset        = Room.objects.all()
    template_name   = 'main/index.html' 
