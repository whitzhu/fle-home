import json 
import os 
import random

import settings

from django.shortcuts import render_to_response, render
from annoying.decorators import render_to

from models import TeamMember, BoardMember, PressArticle, Internship

@render_to("about/team.html")
def team(request):
	return {
		"team_members": TeamMember.objects.order_by("?")
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
