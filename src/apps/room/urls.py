from django.urls import path
from .views import CreateRoom, DetailtRoom, CheckPassowrd, DeleteRoom

app_name = 'room'

urlpatterns = [
    path('<slug:slug>/id<int:pk>/', DetailtRoom.as_view(), name='detail_room'),
    path('<slug:slug>/id<int:pk>/checkpassword/', CheckPassowrd.as_view(), name='checkpassword'),
    path('<slug:slug>/id<int:pk>/delete/', DeleteRoom.as_view(), name='delete_room'),
    path('create/', CreateRoom.as_view(), name='create_new_room'),
]
