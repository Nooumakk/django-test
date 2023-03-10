from django.shortcuts import render
from django.views.generic import FormView, TemplateView


class HomeViev(TemplateView):
    template_name = "home_page.html"

