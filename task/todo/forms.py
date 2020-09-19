from django import forms
from django.forms import ModelForm

from .models import ToDo

class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo # the model we create the form
        fields = ['todo_name'] # which fields to allow in the form