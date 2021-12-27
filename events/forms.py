from django import forms
from .models import client,project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class clientform(forms.ModelForm):
    class Meta:
        model = client
        fields = '__all__'
        widgets={
            'created_at':forms.DateTimeInput(format='%Y.%m.%dT%H:%M:%S.%z'),
        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
	      model = User
	      fields = ['username', 'email', 'password1', 'password2']

class projectForm(forms.ModelForm):
    class Meta:
        model = project
        fields ='__all__'    
       
    