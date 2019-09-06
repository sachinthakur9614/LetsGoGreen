from django.db import models

# Create your models here.


from django.contrib.auth.models import User



class Sapling(models.Model):
	treeName = models.CharField(max_length=100)
	treeDescription = models.TextField(max_length=1000)
	treeImage = models.ImageField(upload_to='images/')
	leaf = models.CharField(max_length=100)
	life = models.IntegerField()
	root = models.CharField(max_length=100)
	stem = models.CharField(max_length=100)
	shoot = models.CharField(max_length=100)
	numOfTree = models.IntegerField()
	us = models.ForeignKey(User,  on_delete=models.CASCADE )

