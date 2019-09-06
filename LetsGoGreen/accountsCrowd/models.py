from django.db import models

# Create your models here.

from django.contrib.auth.models import User




class CrowdUserProfile(models.Model):
	# orgemail = models.EmailField(max_length=100)
	typ = models.IntegerField()
	address = models.TextField(max_length=1000,blank=True,null=True)
	phone = models.BigIntegerField(blank=True)
	state = models.CharField(max_length=100,blank=True,null=True)
	pincode = models.IntegerField(null=True)
	us = models.OneToOneField(User, on_delete=models.CASCADE)
	


