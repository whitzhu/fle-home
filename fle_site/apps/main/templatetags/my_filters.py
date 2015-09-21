from django.template import Library

register = Library()

@register.assignment_tag
def get_twitter_bootstrap_alert_msg_css_name(tags):
    return 'danger' if tags == 'error' else tags
