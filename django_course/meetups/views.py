from django.shortcuts import render

# Create your views here.
def index(requests):
    meetups = [
        {'title': 'First meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
        {'title': 'Second meetup', 'location': 'Paris', 'slug': 'a-second-meetup'}
    ]
    return render(requests, 'meetups/index.html', {'meetups': meetups, 'show_meetups': True})

def meetup_details(requests, meetup_slug):
    print(meetup_slug)
    meetup_details = {
        'title': 'The first meetup',
        'description': 'This is the first meetup!'
    }
    return render(requests, 'meetups/meetup_detail.html', meetup_details)