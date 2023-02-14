from django.urls import path
from .views import homepageView

#Create your urls here

urlpatterns = [
    path('',homepageView,name='home')
]
