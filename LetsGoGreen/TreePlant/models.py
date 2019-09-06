from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# from .models import TreeGrowth
# from TreePlant.models import TreeType, TreeGrowth
class Follower(models.Model):
	followerCount = models.IntegerField()
	followingCount = models.IntegerField()
	us = models.ForeignKey(User,  on_delete=models.CASCADE)






class TreeType(models.Model):
	treeName = models.CharField(max_length=100)
	treeDescription = models.TextField(max_length=100)
	treeAge = models.IntegerField()
	growthTime = models.DateTimeField(default=now)
	
	envEffects = models.CharField(max_length=100)



class TreeGrowth(models.Model):
	firstImage = models.ImageField(upload_to='images/',blank=True)
	secondImage = models.ImageField(upload_to='images/',blank=True)
	thirdImage = models.ImageField(upload_to='images/',blank=True)
	# tree = models.ForeignKey(TreeType, on_delete=models.CASCADE) we might need this field in future t o implement
	us = models.ForeignKey(User,  on_delete=models.CASCADE)



class TreeGrowthApproval(models.Model):
	aprroveTree = models.BooleanField(blank=True)
	us = models.ForeignKey(User,  on_delete=models.CASCADE)

	tree = models.ForeignKey(TreeGrowth,on_delete=models.CASCADE)
	# treeg = models.ForeignKey(TreeGrowth, on_delete=models.CASCADE)



class TreeLocation(models.Model):
	street = models.TextField(max_length=100)
	addressline1= models.TextField(max_length=200)
	addressline2= models.TextField(max_length=200)
	distt = models.CharField(max_length=100)
	state= models.CharField(max_length=100)
	longitude= models.BigIntegerField()
	latitude = models.BigIntegerField()	
	pincode = models.BigIntegerField()
	# tree = models.ForeignKey(TreeType,on_delete=models.CASCADE)// we might add to list the catalog of the Tree CATALOg
	us = models.ForeignKey(User,  on_delete=models.CASCADE)
 

class TreeCatalog(models.Model):
	treeName = models.CharField(max_length=100)
	treeImage = models.ImageField(upload_to='images/')
	treeDescription = models.TextField(max_length=1000)
	lifeTime = models.IntegerField()# paass gthe year field
	leaf = models.CharField(max_length=100,default='qw')
	life = models.IntegerField(default=10)
	root = models.CharField(max_length=100,default='qw')
	stem = models.CharField(max_length=100,default='qw')
	shoot = models.CharField(max_length=100,default='qw')



	def summary(self):
		return self.treeDescription[:150]


