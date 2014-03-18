import json 
import os 
import random

import settings

from annoying.decorators import render_to

# from models import TeamMember, BoardMember, PressArticle, Internship, SupportingOrganization


@render_to("ka-lite/what-is-ka-lite.html")
def what(request):
	return {}

@render_to("ka-lite/how-to-install.html")
def install(request):
	return {}

@render_to("ka-lite/who-is-using-it.html")
def who(request):
	return {}

@render_to("ka-lite/can-i-contribute.html")
def contribute(request):
	return {}

@render_to("ka-lite/faq-and-help.html")
def help(request):
	return {}


