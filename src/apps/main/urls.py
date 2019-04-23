from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import ListRoom


app_name = 'main'

urlpatterns = [
    path('', ListRoom.as_view(), name='main_page'),
    path('room/', include('src.apps.room.urls', namespace='room')),
]
