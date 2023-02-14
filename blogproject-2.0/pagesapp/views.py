from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def error_404_view(request, exception):
    return render(request, "error_page.html")

class HomePageView(TemplateView):
    template_name = 'home.html'