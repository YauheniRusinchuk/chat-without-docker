from django.views.generic.list import ListView
from src.models.room.models import Room


class ListRoom(ListView):

    model           = Room
    template_name   = 'main/index.html'


    def get_queryset(self):
        qs = self.request.GET.get('q')
        if qs is not None:
            return Room.objects.filter(name__icontains=qs)
        return Room.objects.all()
