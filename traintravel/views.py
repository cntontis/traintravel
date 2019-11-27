from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .forms import NewUserForm

# Create your views here.
def trains(request):

	if request.method == 'POST':
		
		source = request.POST['source']
		sourceArr = source.split(',')
		sourceCity = sourceArr[0];
		destination = request.POST['destination']
		destinationArr = destination.split(',')
		destinationCity = destinationArr[0];
		
		startdate = request.POST['startdate']
		startdate = startdate.split('-')
		year = int(startdate[0])
		month = int(startdate[1])
		day = int(startdate[2])
		
		trainClass = request.POST['class']
		
		trains = Train.objects.filter(sourceLocation = sourceCity).filter(destinationLocation=destinationCity).filter(departureDate=datetime.date(year,month,day))
		trains = list(trains)
		
		if (trainClass == 'economy'):
			trains = Train.objects.filter(sourceLocation = sourceCity).filter(destinationLocation=destinationCity).filter(departureDate=datetime.date(year,month,day)).filter(numSeatsRemainingEconomy__gt=0)
			trains = list(trains)
			return render(request, 'trains.html',{"results":"yes", "some_list": trains, "class":trainClass})
		elif (trainClass == 'business'):	
			trains = Train.objects.filter(sourceLocation = sourceCity).filter(destinationLocation=destinationCity).filter(departureDate=datetime.date(year,month,day)).filter(numSeatsRemainingBusiness__gt=0)
			trains = list(trains)
			return render(request, 'trains.html',{"results":"yes", "some_list": trains, "class":trainClass})
		else:
			trains = Train.objects.filter(sourceLocation = sourceCity).filter(destinationLocation=destinationCity).filter(departureDate=datetime.date(year,month,day)).filter(numSeatsRemainingFirst__gt=0)
			trains = list(trains)
			return render(request, 'trains.html',{"results":"yes", "some_list": trains, "class":trainClass})
	else:
		return render(request,
				  "trains.html",)

@csrf_exempt
def hotels(request):
	if request.method == 'POST':
		location = request.POST['location']
		locationArr = location.split(',')
		locationCity = locationArr[0];
		
		startdate = request.POST['startdate']
		enddate = request.POST['enddate']
		
		hotels = Hotel.objects.filter(city = locationCity)
		hotels = list(hotels)
		
		return render(request, 'hotels.html',{"results":"yes", "some_list": hotels})
	else:
		return render(request, 'hotels.html')

def register(request):
	
	if request.method == "POST":
		
		form = NewUserForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, "New Account Created: {}.".format(username))
			login(request, user)
			messages.info(request, "You are now logged in as {}.".format(username))
			return redirect("trains")
		else:
			for msg in form.error_messages:
				messages.error(request, "{}:{}".format(msg,form.error_messages[msg]))	
	
	form = NewUserForm()
	return render(request,
				  "register.html",
				  context = {"form":form})

@csrf_exempt
def login_req(request):

	if request.method == "POST":
		
		form = AuthenticationForm(request , data=request.POST  )
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				messages.info(request, "You are now logged in as {}.".format(username))
				return redirect("hotels")

			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()
	return render(request,
		"login.html",
		{"form":form})


def logout_req(request):
	
	if request.user.is_authenticated:
		logout(request)
		messages.info(request, "Logout Succesfully!")
		return redirect("login")
	else:
		messages.info(request, "You are not Logged In!")
		return redirect("login")