import json 
import os 
import random

from django.shortcuts import render_to_response
from annoying.decorators import render_to

from fle_site import settings

def mission(request):
	return render_to_response("about/mission.html")


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