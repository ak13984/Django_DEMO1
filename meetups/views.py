from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid

from .forms import RegistrationForm
from .models import Meetup, Participant
# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html' , {'meetups':meetups, 'show_meetups':True})

def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                user_email = registration_form.cleaned_data['email']
                participant = Participant.objects.get(email=user_email)
                if participant is None:
                    participant = Participant.objects.create(email = user_email, id = uuid.uuid4()) 
                selected_meetup.particants.add(participant)
                return redirect('confirm-registration')
            
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup':selected_meetup,
            'form':registration_form 
            })
    except Exception as exc:
        print("line number 31")
        print(exc)
        return render(request,'meetups/meetup-details.html',{
        'meetup_found': False,
        
        })


def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')