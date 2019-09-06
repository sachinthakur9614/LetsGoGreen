from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
	phone = models.BigIntegerField()
	profileImage = models.ImageField(upload_to='images/')
	us = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=100,blank=True)
	age= models.IntegerField(blank=True,default=0)
	occupation = models.CharField(max_length=100,blank=True)
	usertype= models.IntegerField()



	# amountRecieve = models.FloatField(blank=True,default=100)
	# follower = models.IntegerField(blank=True)
	# following = models.IntegerField(blank=True)
	# totalTree =   models.IntegerField(blank=True)
	# rank = models.IntegerField(blank=True)







