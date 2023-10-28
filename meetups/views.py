from django.shortcuts import render

meetups = [
    {'title': 'A First Meetup',
     'location': 'Location 1',
     'slug': 'a-first-meetup',
     'description': 'Meetup Description'},

    {'title': 'A Second Meetup',
     'location': 'Location 2',
     'slug': 'a-second-meetup',
     'description': 'Meetup Description'},

    {'title': 'A Third Meetup',
     'location': 'Location 3',
     'slug': 'a-third-meetup',
     'description': 'Meetup Description'}
]


def index(request):
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })


def meetup_details(request, slug):
    selected_meetup = meetups[0]
    for meetup in meetups:
        if meetup['slug'] == slug:
            selected_meetup = meetup

    return render(request, 'meetups/meetup_details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
        'slug': slug
    })
