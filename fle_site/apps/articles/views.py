from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from fle_site.apps.articles.models import Article

def blog_filter_page(request, template='articles/blog_homepage.html'):
    """Display all blog posts, and filters"""
    blog_posts = Article.objects.live().order_by('-publish_date')
    tags = []
    for post in blog_posts:
        tags += post.tags.all()
    tags = set(tags)

    variables = {
        'posts': blog_posts,
        'tags': tags,
    }

    response = render(request, template, variables)
    return response

def display_article(request, year=None, slug=None, template='articles/article_detail.html'):
    """Displays a single article."""

    try:
        article = Article.objects.live(user=request.user).get(publish_date__year=year, slug=slug)
    except Article.DoesNotExist:
        raise Http404

    # make sure the user is logged in if the article requires it
    if article.login_required and not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('auth_login') + '?next=' + request.path)

    # Render top 5 most recent posts in the sidebar 
    blog_posts = Article.objects.live().order_by('-publish_date')

    variables = RequestContext(request, {
        'article': article,
        'disqus_forum': getattr(settings, 'DISQUS_FORUM_SHORTNAME', None),
    })
    response = render(request, template, variables)

    return response

