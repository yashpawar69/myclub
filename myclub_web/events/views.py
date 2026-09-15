from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models  import Event, Venue

from .forms import VenueForm, EventForm, EventFormAdmin
from django.http import HttpResponseRedirect

# Create your views here.
def add_event(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = EventFormAdmin(request.POST)
			if form.is_valid():
					form.save()
					return 	HttpResponseRedirect('/add_event?submitted=True')	
		else:
			form = EventForm(request.POST)
			if form.is_valid():
				form.save()
				event = form.save(commit=False)
				event.manager = request.user # logged in user
				event.save()
				return 	HttpResponseRedirect('/add_event?submitted=True')	
	else:
		# Just Going To The Page, Not Submitting 
		if request.user.is_superuser:
			form = EventFormAdmin
		else:
			form = EventForm

		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})


def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('list-venue')

	return render(request, 'events/update_venue.html',
			    {'venue':venue,
			    'form':form
			    })
def search_venues(request):
	if request.method == "POST":
		searched = request.POST['searched']
		venues = Venue.objects.filter(name__contains=searched)
	
		return render(request, 
		'events/search_venues.html', 
		{'searched':searched,
		'venues':venues})
	else:
		return render(request, 
		'events/search_venues.html', 
		{})

def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	# venue_owner = User.objects.get(pk=venue.owner)

	# Grab the events from that venue
	events = venue.event_set.all()

	return render(request, 'events/show_venue.html', 
		{'venue': venue,
		# 'venue_owner':venue_owner,
		'events':events})

def list_venue(request):
  venues = Venue.objects.all()
  return render(request, 'events/venue.html',
                {'venues': venues})

def add_venue(request):
	submitted = False
	if request.method == "POST":
		form = VenueForm(request.POST,
				    # request.FILES
			)
		if form.is_valid():
			# venue = form.save(commit=False)
			# venue.owner = request.user.id # logged in user
			# venue.save()
			form.save()
			return 	HttpResponseRedirect('/add_venue?submitted=True')	
	else:
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})

def all_events(request):
  event_list = Event.objects.all()
  return render(request, 'events/event_list.html',
                {'event_list':event_list})

def home (request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    name='john'
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #create a calender
    cal = HTMLCalendar().formatmonth(year, month_number)

    #get current year
    now = datetime.now()
    current_year = now.year
    #get current time
    time = now.strftime("%I:%M %p")


    return render(request, 'events/home.html', {"name":name,
                                          "year":year,
                                            "month":month,
                                              "month_number":month_number,
                                                "cal":cal,
                                                  "current_year":current_year,
                                                    "time":time,
                                                      }) 