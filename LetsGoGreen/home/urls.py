from django.urls import path


from home import views 

urlpatterns = [
	path('',views.home,name='home'),
	path('/aboutus',views.addAboutSection,name='aboutus'),
	path('/contacts',views.Contacts,name='contacts'),
	path('/contactForm',views.contacts,name='contactForm'),
	path('contributor',views.contributor,name='contributor')

	



]