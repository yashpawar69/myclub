from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models  import Event, Venue

from .forms import VenueForm, EventForm, EventFormAdmin
from django.http import HttpResponseRedirect, HttpResponse
import csv
#for pdf 
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


#gen pdf file

def venue_pdf(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="venues.pdf"'
	buffer = io.BytesIO()
	p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
	textob = p.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	lines = []
	for venue in Venue.objects.all().order_by('name'):
		lines.append(venue.name)
		lines.append(venue.address)
		lines.append(venue.phone)
		lines.append(venue.website)
		lines.append(venue.state)
		lines.append(" ")
	for line in lines:
		textob.textLine(line)
	p.drawText(textob)
	p.showPage()
	p.save()
	buffer.seek(0)

	return FileResponse(buffer,as_attachment=True,filename=venue_pdf)

# gen csv file
def venue_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="venues.csv"'
	writer = csv.writer(response)
	writer.writerow(['Venue Name', 'Venue Address', 'Venue Phone', 'Venue Website', 'Venue State'])
	for venue in Venue.objects.all().order_by('name'):
		writer.writerow([venue.name, venue.address, venue.phone, venue.website, venue.state])
	return response


#generate text file venue list
def venue_text(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename="venues.txt"'
	lines = []
	for venue in Venue.objects.all():
		lines.append(f'{venue.name}\n{venue.address}\n{venue.phone}\n{venue.website}\n{venue.state}\n\n')
	response.write(''.join(lines))
	return response

def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue.delete()
	return redirect('list-venue')

def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	event.delete()
	return redirect('list_events')


def add_event(request):
    submitted = False

    if request.method == "POST":

        # if request.user.is_superuser:
        #     form = EventFormAdmin(request.POST)

        #     if form.is_valid():
        #         form.save()
        #         return HttpResponseRedirect('/add_event/?submitted=True')

        # else:
            form = EventForm(request.POST)

            if form.is_valid():
                event = form.save(commit=False)
                event.manager = request.user
                event.save()

                return HttpResponseRedirect('/add_event?submitted=True')

    else:

        if request.user.is_superuser:
            form = EventFormAdmin()
        else:
            form = EventForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        'events/add_event.html',
        {
            'form': form,
            'submitted': submitted
        }
    )
def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('list_events')
	return render(request, 'events/update_event.html', {'event':event, 'form':form})


def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('list-venue')

	return render(request, 'events/update_venue.html',
			    {'venue':venue,
			    'form':form})


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
			venue = form.save(commit=False)
			venue.owner = request.user.id # logged in user
			venue.save()
			form.save()
			return 	HttpResponseRedirect('/add_venue?submitted=True')	
	else:
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})

def all_events(request):
  event_list = Event.objects.all().order_by('-event_date')
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