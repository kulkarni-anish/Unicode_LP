from django import forms
from .models import ToDo

class ListForm(forms.ModelForm):
    deadline    = forms.DateTimeInput
    class Meta:
        model = ToDo
        fields = '__all__'