from django.contrib import admin
from .models import Train,Hotel

class TrainAdmin(admin.ModelAdmin):
    fieldsets = [
		("Company", {'fields': ["companyName"]}),
		("From", {"fields": ["srcLocation"]}),
		("To", {"fields": ["destLocation"]}),
		("Departure Date", {"fields": ["departureDate"]}),
		("Departure Time", {"fields": ["departureTime"]}),
		("Price Economy", {"fields": ["priceEconomy"]}),
		("Price Business", {"fields": ["priceBusiness"]}),
		("numSeatsRemainingEconomy", {"fields": ["numSeatsRemainingEconomy"]}),
		("numSeatsRemainingBusiness", {"fields": ["numSeatsRemainingBusiness"]})
	]

class HotelAdmin(admin.ModelAdmin):
    fieldsets = [
		("Company", {'fields': ["companyName"]}),
		("Price", {'fields': ["dailyPrice"]}),
		("Address", {'fields': ["address"]}),
		("Location", {'fields': ["location"]}),
	]

admin.site.register(Train, TrainAdmin)
admin.site.register(Hotel, HotelAdmin)
