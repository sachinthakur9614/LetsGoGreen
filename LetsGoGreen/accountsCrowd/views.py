from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from accounts.models import UserProfile
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.core.mail  import send_mail
from accountsCrowd.models import CrowdUserProfile




def cLogin(request):

	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		if email=='':
			return render(request,'login.html',{'errorr':'Email Field is not filled'})
		if password=='':
			return render(request,'login.html',{'errorr':'Password Field is not filled'})
	


		user = auth.authenticate(username=email,password=password)
		# print(user)
		
		# print(key) #33
		if user is not None:
			key = user._get_pk_val()
			# user_1 = list(UserProfile.objects.values_list('type_usr','id').filter(id=key).values('type_usr'))
			# user_type = user_1[0]
			# var=user_type['type_usr']
			# user_1 = list(CrowdUserProfile.objects.values_list('typ','id').filter(id=key).values('typ'))
			# user_type = user_1[1]
			# var=user_type['typ']

			# if user_type['typ']==100 or user_type['typ']==200 or user_type==300:
			
			if CrowdUserProfile.objects.filter(us_id=key,typ=100).exists():
				auth.login(request,user)
				return redirect('contribution')
			
			elif CrowdUserProfile.objects.filter(us_id=key,typ=200).exists():
				auth.login(request,user)
				return redirect('contribution')
			elif CrowdUserProfile.objects.filter(us_id=key,typ=300).exists():
				auth.login(request,user)
				return redirect('contribution')
			else:
				return render(request,'login_crowd.html',{'errorr':'invalid credentials'})
			


			# if profileinfo.typ=='100' or profileinfo.typ==200 or profileinfo.typ==300:
			# request.session['userid']=request.user.id
			# return render(request,'contribution.html',{'error':'invalid credentials'})
			

			



				# return redirect('participantIndex')
				
		else:
			return render(request,'login_crowd.html',{'errorr':'Invalid Credentials'})
	
			# messages.error(request,'invalid credentials')

	# return render(request,'login_crowd.html')




def cSignup(request):
	if request.method=='POST':
		orgName = request.POST['orgName']
		userName = request.POST['userName']
		email = request.POST['email']
		password = request.POST['password']
		confirmPassword = request.POST['confirmPassword']
		mobile = request.POST['mobile']
		typ = request.POST['type']
		addres="kk"
		state ='00'
		pincode=1980
		if password == confirmPassword:
			if User.objects.filter(username=userName).exists():
				# message.error(request,"That username is taken")
				return render(request,'login_crowd.html',{'error':'user already exist please login with credentials'})
			else:
				if User.objects.filter(email=email).exists():
					# message.error(request,"That email is been use")
					return render(request,'login_crowd.html',{'error': ' Email already  in Use '})
				else:
					user = User.objects.create_user(username=userName,password=password,email=email,first_name=orgName)


					user.save()
					userr = User.objects.get(username=userName).pk
					crowuser =  CrowdUserProfile(typ=typ,address=addres,phone=mobile,state=state,pincode=pincode,us_id=userr)
					crowuser.save()
					send_mail(' Successfull Registration on LetsGoGreen',
								'HI '+ orgName+',\n Thank you coming ahead for Environment Contribution',
								'sachin.thakur9614@gmail.com',
								[email,'sachin.thakur@mca.christuniversity.in',],
								fail_silently =False)
					messages.success(request,'You are now registered in')
					return render(request,'login_crowd.html',{'register':'Registration is Successfull'})
		elif orgName=='':
			messages.error(request,'First Name  field  is empty')
			return render(request,'login_crowd.html',{'error':'OrgName/NGO/Individual  field  is empty'})
			
			

		elif userName=='':
			messages.error(request,'User Name  field  is empty')
			return render(request,'login_crowd.html',{'error':'User Name  field  is empty'})
			

		elif password=='':
			messages.error(request,'Password  field  is empty')
			return render(request,'login_crowd.html',{'error':'Password  field  is empty'})
			
		elif confirmPassword=='':
			messages.error(request,'Confirm Password  field  is empty')
			return render(request,'login_crowd.html',{'error':'Confirm Password  field  is empty'})
			

		elif mobile=='':
			messages.error(request,'Mobile No  field  is empty')
			return render(request,'login_crowd.html',{'error':'Mobile No  field  is empty'})
				

		





		

		return render(request,'login_crowd.html')




def accountsCrowds(request):
	return render(request,'login_crowd.html')





def accountsDonte(request):
	return render(request,'login.html')


def accountCro(request):
	return render(request,'login.html')

def signup(request):
	if request.method=='POST':
		firstName = request.POST['firstName']
		lastName = request.POST['lastName']
		userName = request.POST['userName']
		email = request.POST['email']
		password = request.POST['password']
		confirmPassword = request.POST['confirmPassword']
		mobile = request.POST['mobile']
		profileImage = request.POST['profileImage']
		usertype =12

		if password == confirmPassword:
			if User.objects.filter(username=userName).exists():
				# message.error(request,"That username is taken")
				return redirect('accounts')
			else:
				if User.objects.filter(email=email).exists():
					# message.error(request,"That email is been use")
					return redirect('accounts')
				else:
					user = User.objects.create_user(username=userName,password=password,email=email,first_name=firstName,last_name=lastName)
					user.save()
					
					
					userr = User.objects.get(username=userName).pk
					
					useo = UserProfile(phone=mobile,profileImage=profileImage,us_id=userr)
					useo.save()
					send_mail(' Successfull Registration on LetsGoGreen',
								'HI '+ firstName+',\n Thank you coming ahead for Environment Contribution',
								'sachin.thakur9614@gmail.com',
								[email,'sachin.thakur@mca.christuniversity.in',],
								fail_silently =False)

				
					messages.success(request,'You are now registered in')
					return redirect('contribution')
		elif firstName=='':
			messages.error(request,'First Name  field  is empty')
			return render(request,'login.html',{'error':'First Name  field  is empty'})
			
		elif lastName=='':
			messages.error(request,'Last Name  field  is empty')
			return render(request,'login.html',{'error':'Last Name  field  is empty'})
			

		elif userName=='':
			messages.error(request,'User Name  field  is empty')
			return render(request,'login.html',{'error':'User Name  field  is empty'})
			

		elif password=='':
			messages.error(request,'Password  field  is empty')
			return render(request,'login.html',{'error':'Password  field  is empty'})
			
		elif confirmPassword=='':
			messages.error(request,'Confirm Password  field  is empty')
			return render(request,'login.html',{'error':'Confirm Password  field  is empty'})
			

		elif mobile=='':
			messages.error(request,'Mobile No  field  is empty')
			return render(request,'login.html',{'error':'Mobile No  field  is empty'})
			

		elif profileImage=='':
			messages.error(request,'Profile Image  field  is empty')
			return render(request,'login.html',{'error':'Profile Image  field  is empty'})
			

def logout(request):
	if request.method=='POST':
		auth.logout(request)
		return redirect('home') 



def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(username=email,password=password)

		# print(user)

		
		# print(key) #33
		if user is not None:
			key = user._get_pk_val()
			user_1 = list(UserProfile.objects.values_list('usertype','id').filter(id=key).values('usertype'))
			# user_type = user_1[0]
			# var=user_type['type_usr']	
			

			auth.login(request,user)
			request.session['userid']=key


			profileinfo = UserProfile.objects.filter(us_id=request.user.id)

			return render(request,'nav_plant_tree.html',{'profileinfo':profileinfo})
				# return redirect('participantIndex')
				
		else:
			messages.error(request,'invalid credentials')
			return redirect('login')
	else:
		return render(request,'login.html')



