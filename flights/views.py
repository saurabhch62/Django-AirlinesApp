from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Flight,Airport, Passenger


# Create your views here.

def index(request):
	return render(request, "flights/index.html", {
		"flights" : Flight.objects.all()
		})

def flight(request, flight_id):
	flight = Flight.objects.get(id=flight_id)
	
    
	return render(request, "flights/flight.html", {
			"flight": flight,
			"passenger":flight.passenger.all(), #we can do this because passenger is a related name (passenger associated with flights)
			"non_passengers" : Passenger.objects.exclude(passenger=flight).all() #passenger not in any flight
		})

def book(request, flight_id):
	

	if request.method == "POST":

		#accessing the flight
		flight = Flight.objects.get(id=flight_id)

		#accessing passenger id from form
		passenger_id = request.POST["passenger"]


		#accessing passenger
		passenger = Passenger.objects.get(pk=passenger_id)

		#add passenger
		flight.passenger.add(passenger)

		return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))
						#the comma implies that it is a list or tuple not string