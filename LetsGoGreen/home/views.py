

# Create your views here.


from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail  import send_mail
from .models import AboutDescription 
from .models import Contact
from .models import TeamInfo
from .models import OurServices

from django.core.mail  import send_mail
from TreePlant.models import  TreeGrowth

from .models import Slider
from django.contrib.auth.models import User
from accounts.models import UserProfile




def contributor(request):
	count=0;
	treeGrowth = TreeGrowth.objects.filter(us_id=request.user.id).count()
	info =  User.objects.filter()
	# user_1 = list(UserProfile.objects.values_list('usertype','id').filter(id=key).values('usertype'))
				
	return render(request,'contributor.html',{'treeGrowth':treeGrowth})





def Contacts(request):
	return render(request,'contact.html')







def home(request):
	slide= Slider.objects
	aboutDesc = AboutDescription.objects
	teaminfo = TeamInfo.objects
	services = OurServices.objects	


	return render(request,'index.html',{'slide':slide,'aboutDesc':aboutDesc,'teaminfo':teaminfo,'services':services})






def addAboutSection(request):
	aboutDesc = AboutDescription.objects
	teaminfo = TeamInfo.objects
	services = OurServices.objects	
	return render(request,'aboutus.html',{'aboutDesc':aboutDesc,'teaminfo':teaminfo,'services':services})



def contacts(request):
	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		phone = request.POST['mobile']
		message = request.POST['message']

		contact =Contact(name= name,email=email,subject=subject,phone =phone,message=message )
		send_mail('Subject' +subject,
			'Message'+ message + 'Will Contact your soon',
			'sachin.thakur9614@gmail.com',
			[email,'sachin.thakur@mca.christuniversity.in',],
			fail_silently =False




			)


		contact.save()
		# send Email
		send_mail('Subject' +subject,
			'Message'+ message + 'Will Contact your soon',
			'sachin.thakur9614@gmail.com',
			[email,'sachin.thakur@mca.christuniversity.in',],
			fail_silently =False




			)

		messages.success(request,'Your request has been submited, We will contact you shortly') 
		# mail.send()
		return render(request,'contact.html')



