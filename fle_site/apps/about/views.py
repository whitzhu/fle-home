import json
import os
import random

from django.conf import settings

from annoying.decorators import render_to

from models import TeamMember, BoardMember, PressArticle, Internship, Job, SupportingOrganization

@render_to("about/team.html")
def team(request):
    return {
        "team_members": TeamMember.objects.current(),
        "alumni": TeamMember.objects.alumni(),
    }

@render_to("about/board.html")
def board(request):
    return {
        "board_members": BoardMember.objects.order_by("?")
    }

@render_to("about/press.html")
def press(request):
    return {
        "press_articles": PressArticle.objects.order_by('-publish_date')
    }

@render_to("about/internships.html")
def internships(request):
    return {
        "internships": Internship.objects.all()
    }

@render_to("about/jobs.html")
def jobs(request):
    return {
        "jobs": Job.objects.active()
    }

@render_to("about/supporters.html")
def supporters(request):
    sponsors = SupportingOrganization.objects.filter(organization_type__title="sponsor")
    partners = SupportingOrganization.objects.filter(organization_type__title="partner")
    return {
        "sponsors": sponsors,
        "partners": partners
    }
