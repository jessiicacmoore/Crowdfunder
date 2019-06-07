from django.forms import ModelForm
from .models import Project, 

def CreateProject(ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'picture',
            'description',
            'funding_goal',
            'start_date',
            'end_date',
            'end_date',
        ]
