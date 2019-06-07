from django.forms import CharField, PasswordInput, Form, ModelForm
from django import forms
from crowdfunder.models import Project

import datetime as dt

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())

class CreateProject(ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': dt.date.today() }))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': dt.date.today() }))

    class Meta:
        model = Project
        fields = [
            'title',
            'picture',
            'description',
            'category',
            'funding_goal',
            'start_date',
            'end_date',
            'end_date',
        ]