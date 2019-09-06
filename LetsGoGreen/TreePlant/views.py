from django.shortcuts import render,redirect
from accounts.models import UserProfile
from .models import TreeCatalog,TreeGrowth,TreeLocation
from django.contrib.auth.models import User

def plantTree(request):
	return render(request,'plant_tree.html')


def vedio(request):
	return render(request,'video.html')

def placeAvailable(request):
	return render(request,'place_available.html')


def userSuggestion(request):
	info = User.objects
	# usepro = UserProfile.objects.get(us_id=info.id)

	return render(request,'user_suggestion.html',{'info':info})

def followers(request):
	return render(request,'user_profile.html')



def treeLocation(request):
	return render(request,'tree_location.html')

def treeLocationForm(request):
	if request.method=='POST':
		street = request.POST['street']
		addressline1 = request.POST['addressline1']
		addressline2 = request.POST['addressline2']
		distt = request.POST['distt']
		state = request.POST['state']
		longitude = request.POST['longitude']
		latitude = request.POST['latitude']
		pincode = request.POST['latitude']


		if street=='':
			return render(request,'tree_location.html',{'error':'Street Name is empty '})		
		else:
			street = request.POST['street']
		if addressline1=='':
			return render(request,'tree_location.html',{'error':'Address Line1   Field  is empty'})
		else: 
			addressline1 = request.POST['addressline1']
		
		if addressline2 =='':
			return render(request,'tree_location.html',{'error':'Address Line2   Field  is empty'})
		else:
			addressline2 = request.POST['addressline2']
		
		if distt=='':
			return render(request,'tree_location.html',{'error':'District   Field  is empty'})
		else:
			distt = request.POST['distt']
			
		if state=='':
			return render(request,'tree_location.html',{'error':'State    Field is not selected'})
		else:
			state = request.POST['state']
		
		if pincode=='':
			return render(request,'tree_location.html',{'error':'Pincode   Field  is empty'})
		else:
			pincode = request.POST['latitude']
	




		treeLocation = TreeLocation(street=street,addressline1=addressline1,addressline2=addressline2,distt=distt,state=state,longitude=longitude,latitude=latitude,pincode=pincode,us_id=request.user.id)
		treeLocation.save()

		return render(request,'plant_tree.html')






  # street,addressline1,addressline2,distt,state,longitude,latitude,
  





def treeCount(request):
	count=0;
	treeGrowth = TreeGrowth.objects.filter(us_id=request.user.id)
	print(" tree count",treeGrowth)

	return render(request,'tree_location.html')

def editeTreeGrowth(request):
	
	return render(request,'tree_location.html',{'info':info})



def treeImagesUpload(request):
	if request.method=='POST':
		firstImage = request.POST['firstImage']
		secondImage =request.POST['secondImage']
		thirdImage = request.POST['thirdImage']
		if firstImage=='':
			return render(request,'tree_images.html',{'error':'First Image   field  is empty'})		
		else:
			firstImage = request.POST['firstImage']

		if secondImage=='':
			return render(request,'tree_images.html',{'error':'Second Image   field  is empty'})
		else:
			secondImage =request.POST['secondImage']

		if thirdImage =='':
			return render(request,'tree_images.html',{'error':'Third Image   field  is empty'})

		else:
			thirdImage = request.POST['thirdImage']



		treeGrowth = TreeGrowth(firstImage=firstImage,secondImage=secondImage,thirdImage=thirdImage,us_id=request.user.id)
		treeGrowth.save()
		count=0;
		treeGrowth = TreeGrowth.objects.filter(us_id=request.user.id).count()
		print(" tree count",treeGrowth)
		return render(request,'plant_tree.html')


def treeImages(request):
	treeCount = TreeGrowth.objects.filter(us_id=request.user.id).count()
	# print(" tree count",treeGrowt)
	info = User.objects
	return render(request,'tree_images.html',{'treeCount':treeCount,'info':info})







def treeCatalogInfo(request,id):
	tree = TreeCatalog.objects.get(pk=id)
	info = User.objects
	
	return render(request,'tree_catalog_info.html',{'tree': tree,'info':info})




def treeCatalog(request):
	treeCatalog = TreeCatalog.objects
	return render(request,'tree_catalog.html',{'treeCatalog': treeCatalog})


def deleteAccount(request):

	return render(request,'delete_account.html')

def deletedAccount(request):
	use = User.objects.filter(username= request.user.username).delete()
	return redirect('home')





def userProfile(request):
	info = User.objects
	
	profileinfo = UserProfile.objects.filter(us_id=request.user.id)
	context ={'profileinfo':profileinfo,
	 			'info':info
	 			}



	
	return render(request,'user_profile.html',context)

def editProfile(request):
	profileinfo = UserProfile.objects.filter(us_id=request.user.id)
	if request.method=='POST':
		first_name = request.POST['firstName']
		last_name =request.POST['lastName']
		profileImage = request.POST['profileImage']
		phone = request.POST['phone']
		gender = request.POST['gender']
		age = request.POST['age']
		occupation = request.POST['occupation']
		idd= request.POST['id']

		
		if first_name=='':
			return render(request,'tree_images.html',{'error':'First Name    field  is empty'})		

		else:
			first_name = request.POST['firstName']

		if last_name=='':
			return render(request,'tree_images.html',{'error':'Last Name    field  is empty'})		

		else:
			last_name =request.POST['lastName']
		if profileImage=='':

			profileImage=request.POST['img']
		else:
			profileImage = request.POST['profileImage']

		if phone=='':

			return render(request,'tree_images.html',{'error':'Phone  field  is empty'})		

		else:
			phone = request.POST['phone']
			
		if gender=='':
			return render(request,'tree_images.html',{'error':'Gender   field  is empty'})		

		else:	
			gender = request.POST['gender']
	


		if age=='':

			return render(request,'tree_images.html',{'error':'Age   field  is empty'})		

		else:
			age = request.POST['age']


		if occupation=='':

			return render(request,'tree_images.html',{'error':'Occupation    field  is empty'})		

		else:
			occupation = request.POST['occupation']
		


  # occupation,gender,profileImage,phone,firstName, lastName
		userpro=User(id=request.user.id,username=request.user.username,password=request.user.password,email=request.user.email,first_name=first_name,last_name=last_name)
		userpro.save()
		# forid=UserProfile.objects.get(us_id=request.user.id)
		print("id is",idd)
		userProfile = UserProfile(id=idd, phone=phone,profileImage=profileImage,us_id=request.user.id,gender=gender,age=age,occupation=occupation)
		userProfile.save()
		# useo = UserProfile(phone=mobile,profileImage=profileImage,us_id=userr)
					

		return render(request,'user_profile.html',{'profileinfo':profileinfo})
