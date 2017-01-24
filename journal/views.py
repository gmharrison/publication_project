from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"


class MainZineView(TemplateView):
    template_name = "zine_content.html"


class AboutView(TemplateView):
    template_name = "about.html"