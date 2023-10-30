from django.shortcuts import render
from .models import Meetup
from .forms import RegistrationForm

meetups = Meetup.objects.all()


def index(request):
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })


def meetup_details(request, slug):
    try:
        selected_meetup = Meetup.objects.get(slug=slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': False,
        })
