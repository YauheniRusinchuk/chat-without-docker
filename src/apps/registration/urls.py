from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import SignUp

app_name = 'create'


urlpatterns = [
    path('account/', SignUp.as_view(), name='create_account'),
]
