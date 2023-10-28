from django.shortcuts import render

meetups = [
    {'title': 'A First Meetup',
     'location': 'Location 1',
     'slug': 'a-first-meetup'},

    {'title': 'A Second Meetup',
     'location': 'Location 2',
     'slug': 'a-second-meetup'},

    {'title': 'A Third Meetup',
     'location': 'Location 3',
     'slug': 'a-third-meetup'}
]


def index(request):
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })


def meetup_details(request):
    selected_meetup = {'title': 'A First Meetup',
                       'location': 'Location 1',
                       'slug': 'a-first-meetup',
                       'description': 'Meetup Description'}

    return render(request, 'meetups/meetup_details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
    })
