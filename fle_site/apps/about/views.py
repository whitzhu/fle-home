import json 
import os 
import random

from django.shortcuts import render_to_response, render
from annoying.decorators import render_to

from fle_site import settings
from models import AboutSection

def mission(request):
	about_sections = AboutSection.objects.all()
	context = {
		"about_sections": about_sections
	}
	return render(request, "about/mission.html", context)


@render_to("about/team.html")
def team(request):
    team = json.load(open(os.path.join(settings.PROJECT_PATH, "data/team.json")))
    random.shuffle(team)
    return {
        "team": team
    }


def board(request):
	return render_to_response("about/board.html")


def supporters(request):
	return render_to_response("about/supporters.html")