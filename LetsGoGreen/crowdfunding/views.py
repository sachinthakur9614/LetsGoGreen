
from django.shortcuts import render


from accounts.models import UserProfile
from django.contrib.auth.models import User

from .models import Sapling

from TreePlant.models import TreeCatalog
 
from accountsCrowd.models import  CrowdUserProfile





def treeanalysis(request):
	return render(request,'analysis.html')



def catalogtreemore(request,id):
	tree = TreeCatalog.objects.get(pk=id)
	info = User.objects
	
	return render(request,'catalog_tree_more.html',{'tree': tree,'info':info})




def catalogtree(request):
	treeCatalog = TreeCatalog.objects
	return render(request,'catalog_tree.html',{'treeCatalog': treeCatalog})




def userInfo(request):

	info = User.objects
	
	profileinfo =CrowdUserProfile.objects.filter(us_id=request.user.id)
	context ={'profileinfo':profileinfo,
	 			'info':info
	 			}

	cuser = objects.filter(us_id=request.user.id)
	return render(request,'crowd_user_profile.html',context)



def addSapling(request):
	if request.method =='POST':
		treeName = request.POST['treeName']
		treeDescription = request.POST['treeDescription']
		treeImage = request.POST['treeImage']
		leaf = request.POST['leaf']
		life = request.POST['life']
		root = request.POST['root']
		stem = request.POST['stem']
		shoot = request.POST['shoot']
		numOfTree = request.POST['numOfTree']
		sap = Sapling(treeName =treeName,treeDescription=treeDescription,treeImage=treeImage,leaf=leaf,life=life,root=root,stem=stem,shoot=shoot,numOfTree=numOfTree,us_id=request.user.id)
		sap.save()
		return render(request,'crowd_sapling.html',{'register':'added sapling'})



def sapling(request):
	return render(request,'crowd_sapling.html')



def paymentGateways(request):

	return render(request,'payment_gateways.html')




def index(request):
	return render(request,'crowd_funding_profile.html')


def contribution(request):
	userinf = User.objects.filter(id=request.user.id)
	print("userinfo is")
	return render(request,'crowd_funding_profile.html',{userinf:'userinfo'})


def updateUserProfile(request):
	if request.method=='POST':

		userinfo = User.objects
		firstName = request.POST['firstName']
		lastName = request.POST['lastName']
		userName = request.POST['userName']
		email = request.POST['email']
		password = request.POST['password']
		confirmPassword = request.POST['confirmPassword']
		mobile = request.POST['mobile']
		profileImage = request.POST['profileImage']



		return render(request,'crowd_funding_profile.html',{userinfo:'userinfo'})
