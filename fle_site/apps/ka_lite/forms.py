from django import forms
from django.forms import ModelForm

from .models import DeploymentStory, Gallery, Picture


class DeploymentStoryForm(ModelForm):
    class Meta:
        model = DeploymentStory
        exclude = ('guest_blog_post', 'photo_gallery')

    def __init__(self, *args, **kwargs):
            super(DeploymentStoryForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'