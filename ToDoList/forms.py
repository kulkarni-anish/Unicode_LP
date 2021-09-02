from django import forms
from .models import ToDo, MyUserModel
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class ListForm(forms.ModelForm):
    deadline    = forms.DateTimeInput
    class Meta:
        model = ToDo
        exclude = ['updates']


class MyUserCreationForm(UserCreationForm): #This need to be rewritten for it to work properly                                       
    class Meta:                             #If not rewritten it will only render username and password in the form
        model   = MyUserModel       
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email','profile_picture')
        #Extending fields from the default form

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = MyUserModel
        fields = ['username','first_name','last_name','email','profile_picture']
        #fields = UserChangeForm.Meta.fields + ('first_name','last_name','email',)