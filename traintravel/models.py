from django.db import models

# Create your models here.


class User(models.Model):
	username = models.CharField(max_length=40, unique=True, primary_key=True)
	email = models.CharField(max_length=35, unique=True)
	password = models.CharField(max_length=20)


class Train(models.Model):
	companyName = models.CharField(max_length=30)
	srcLocation = models.CharField(max_length=30)
	destLocation = models.CharField(max_length=30)
	departureDate = models.DateField()
	departureTime = models.TimeField()
	priceEconomy = models.DecimalField(max_digits=6, decimal_places=2)
	priceBusiness = models.DecimalField(max_digits=6, decimal_places=2)
	numSeatsRemainingEconomy = models.IntegerField()
	numSeatsRemainingBusiness = models.IntegerField()


class Hotel(models.Model):
	dailyPrice = models.DecimalField(max_digits=6, decimal_places=2)
	address = models.CharField(max_length=30)
	location = models.CharField(max_length=30)
	companyName = models.CharField(max_length=30, default='hotel')


class Payment(models.Model):
	PAYMENT_TYPES = [('credit', 'Credit'), ('debit', 'Debit')]
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	paymentType = models.CharField(choices=PAYMENT_TYPES, max_length=6)
	cardNo = models.CharField(max_length=16)