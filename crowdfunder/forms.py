from django.forms import CharField, PasswordInput, Form, ModelForm
from django import forms
from crowdfunder.models import *

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
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Your project title'}),
            'picture': forms.URLInput(attrs={'placeholder': 'Picture url'}),
            'description': forms.Textarea(attrs={'placeholder': 'Your project description'}),
        }

class MakeDonation(ModelForm):
    class Meta:
        model = Donation
        fields = [
            'user',
            'project',
            'donation_amount',
        ]
        widgets = {
            'user': forms.HiddenInput(),
            'project': forms.HiddenInput(),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        donation_user = cleaned_data.get("user")
        project = cleaned_data.get("project")

        if donation_user == project.owner:
            raise forms.ValidationError("You cannot donate to your own project!")

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'user',
            'project',
            'message'
        ]
        widgets = {
            'user': forms.HiddenInput(),
            'project': forms.HiddenInput()
        }