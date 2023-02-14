from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class OurProjectsView(TemplateView):
    template_name = 'our_projects.html'

class OurTeamView(TemplateView):
    template_name = "our_team.html"

class InterestingFactsView(TemplateView):
    template_name = 'interesting_facts.html'