from django.urls import path
from .views import HomePageView,AboutPageView,OurProjectsView,OurTeamView,InterestingFactsView

urlpatterns = [
    path('about/',AboutPageView.as_view(),name='about'),
    path('facts/',InterestingFactsView.as_view(),name='interesting_facts'),
    path('our_projects/',OurProjectsView.as_view(),name='our_projects'),
    path('our_team/',OurTeamView.as_view(),name='our_team'),
    path('',HomePageView.as_view(),name='home'),
]
