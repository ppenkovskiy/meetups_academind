from django.shortcuts import render, redirect
from .models import Meetup, Participant
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
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration-page')
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': False,
        })


def confirm_registration(request):
    return render(request, 'meetups/registration_success.html')