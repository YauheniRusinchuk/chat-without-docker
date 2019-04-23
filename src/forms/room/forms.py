from django import forms
from src.models.room.models import Room
from django.contrib.auth.hashers import make_password


class FormRoom(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model   = Room
        fields  = [
            'name',
            'password',
        ]


    def clean_password(self):
        hashed_pswd = make_password(self.cleaned_data.get('password'))
        return hashed_pswd
