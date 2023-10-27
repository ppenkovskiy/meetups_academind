from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='starting-page'),
    path('meetups/', index, name='starting-page'),
]