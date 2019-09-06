from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.mail  import send_mail





def accountsDonte(request):
	return render(request,'login.html')


def account(request):
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
		usertype = 11

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
					
					useo = UserProfile(phone=mobile,profileImage=profileImage,us_id=userr,usertype=usertype)
					useo.save()
					send_mail(' Successfull Registration on LetsGoGreen',
								'HI '+ firstName+',\n Thank you coming ahead for Environment Contribution',
								'sachin.thakur9614@gmail.com',
								[email,'sachin.thakur@mca.christuniversity.in',],
								fail_silently =False)

				
					messages.success(request,'You are now registered in')
					return render(request,'login.html',{'register':'Registration is Successfull'})
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

			auth.login(request,user)
			request.session['userid']=request.user.id


			profileinfo = UserProfile.objects.filter(us_id=request.user.id)

			return render(request,'plant_tree.html',{'profileinfo':profileinfo})
				# return redirect('participantIndex')
				
		else:
			return render(request,'login.html',{'errorr':'Invalid Credentials'})
	
			# messages.error(request,'invalid credentials')

			# return 
	else:
		return render(request,'login.html')



