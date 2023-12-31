from django.urls import path
import meetups.views
from . import views


urlpatterns = [
    path('', views.index, name='starting-page'),
    path('', views.index, name='starting-page'),
    path('<slug:slug>/success/', views.confirm_registration, name='confirm-registration-page'),
    path('<slug:slug>', views.meetup_details, name='meetup-detail-page'),
]