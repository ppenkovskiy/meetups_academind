from django.urls import path
import meetups.views
from . import views


urlpatterns = [
    path('', views.index, name='starting-page'),
    path('meetups/', views.index, name='starting-page'),
    path('meetups/<slug:slug>', views.meetup_details, name='meetup-detail-page'),
]