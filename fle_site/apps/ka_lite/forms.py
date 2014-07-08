from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory

from file_resubmit.admin import AdminResubmitImageWidget

from .models import DeploymentStory, Gallery, Picture


class DeploymentStoryForm(ModelForm):
    class Meta:
        model = DeploymentStory
        exclude = ('guest_blog_post', 'photo_gallery', 'latitude', 'longitude', 'title', 'published', 'slug', 'start_date')

    def __init__(self, *args, **kwargs):
            super(DeploymentStoryForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'


class PictureForm(ModelForm):
    exclude=("sort_order", "gallery", 'title',)

    class Meta:
        widgets = {
            'picture': AdminResubmitImageWidget,
        }

    def __init__(self, *args, **kwargs):
            super(PictureForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'



PictureFormSet = modelformset_factory(Picture, form=PictureForm, exclude=("sort_order", "gallery", 'title',), extra=5)
