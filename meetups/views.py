from django.shortcuts import render


def index(request):
    meetups = [
        {'title': 'A First Meetup'},
        {'title': 'A Second Meetup'},
        {'title': 'A Third Meetup'},
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': False,
        'meetups': meetups,
    })