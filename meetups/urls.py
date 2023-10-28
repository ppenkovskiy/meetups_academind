from django.urls import path

import meetups.views
from .views import index, meetup_details


urlpatterns = [
    path('', index, name='starting-page'),
    path('meetups/', index, name='starting-page'),
    path('meetups/meetup_details/', meetup_details, name='meetup-detail-page'),
]