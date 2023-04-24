from django.shortcuts import render
from django.views.generic import DetailView, ListView
from bakery.views import BuildableDetailView, BuildableListView, BuildableTemplateView

from .models import Thing, Quest

class ThingList(ListView):
    model = Thing

class QuestList(ListView):
    model = Quest

class ThingView(DetailView):
    model = Thing

class QuestView(DetailView):
    model = Quest

# Bakery views
class BakeryThingView(BuildableDetailView):
    model = Thing
    template_name = 'quest/thing_detail.html'

class BakeryThingList(BuildableListView):
    model = Thing
    template_name = 'quest/thing_list.html'
    build_path = 'things/index.html'

class BakeryHomeView(BuildableTemplateView):
    build_path = 'index.html'
    template_name = 'quest/index.html'
