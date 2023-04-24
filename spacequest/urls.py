from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.flatpages import views


from quest.views import QuestView, ThingView, QuestList, ThingList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("quests/",QuestList.as_view()),
    path("things/", ThingList.as_view()),
    path('quest/<slug:slug>/', QuestView.as_view(), name="quest"),
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('', TemplateView.as_view(template_name='quest/index.html'), name='home'),
    path('<slug:slug>/',ThingView.as_view(), name="thing"),
    ]
