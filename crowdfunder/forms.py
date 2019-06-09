from django.forms import CharField, PasswordInput, Form, ModelForm
from django import forms
from crowdfunder.models import Project
from datetime import date, datetime
from django.core.exceptions import ValidationError
from pytz import timezone

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())

class CreateProject(ModelForm):
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
    def clean_published_date(self):
        # localizing both dates
        publishedDate = self.cleaned_data['published_date']
        presentDate = date.fromtimestamp(datetime.now(timezone('America/Toronto')).timestamp())
        print(presentDate)
        print(publishedDate)
        isDraft = self.cleaned_data['draft']
        if isDraft:
            if publishedDate < presentDate:
                raise ValidationError('Specified date must be in the future!')
            else:
                return publishedDate
        else:
            if publishedDate > presentDate:
                raise ValidationError('Specified date must be in the past!')
            else:
                return publishedDate
