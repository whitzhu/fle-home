import logging

from django import forms
from django.utils.translation import ugettext_lazy as _
from models import Article, Tag

log = logging.getLogger('articles.forms')

def tag(name):
    """Returns a Tag object for the given name"""

    slug = Tag.clean_tag(name)

    log.debug('Looking for Tag with slug "%s"...' % (slug,))
    t, created = Tag.objects.get_or_create(slug=slug, defaults={'name': name})
    log.debug('Found Tag %s. Name: %s Slug: %s Created: %s' % (t.pk, t.name, t.slug, created))

    if not t.name:
        t.name = name
        t.save()

    return t

class ArticleAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """Sets the list of tags to be a string"""

        instance = kwargs.get('instance', None)
        if instance:
            init = kwargs.get('initial', {})
            kwargs['initial'] = init

        super(ArticleAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Article

    class Media:
        css = {
            'all': ('/css/jquery.autocomplete.css',),
        }
        js = (
            '/js/jquery-1.4.1.min.js',
            '/js/jquery.bgiframe.min.js',
            '/js/jquery.autocomplete.pack.js',
            '/js/tag_autocomplete.js',
        )

