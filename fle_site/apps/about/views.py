import json 
import os 
import random

from django.shortcuts import render_to_response, render
from annoying.decorators import render_to

from fle_site import settings
from models import TeamMember, BoardMember, PressArticle, Internship

def mission(request):
	return render_to_response("about/mission.html")


def team(request):
	team_members = list(TeamMember.objects.all())
	random.shuffle(team_members)
	context = {
		"team_members": team_members
	}
	return render(request, "about/team.html", context)


def board(request):
	board_members = list(BoardMember.objects.all())
	random.shuffle(board_members)
	context = {
		"board_members": board_members
	}
	return render(request, "about/board.html", context)


def supporters(request):
	return render_to_response("about/supporters.html")


def press(request):
	press_articles = PressArticle.objects.order_by('-publish_date')
	context = {
		"press_articles": press_articles
	}
	return render(request, "about/press.html", context)


def internships(request):
	internships = Internship.objects.all()
	context = {
		"internships": internships
	}
	return render(request, "about/internships.html", context)