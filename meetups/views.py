from django.shortcuts import render
from .models import Meetup

meetups = Meetup.objects.all()


def index(request):
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })


def meetup_details(request, slug):
    try:
        selected_meetup = Meetup.objects.get(slug=slug)

        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_description': selected_meetup.description,
            'slug': slug
        })
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': False,

        })
