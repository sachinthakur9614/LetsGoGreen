from django.contrib import admin
from django.urls import path,include
from accounts import views

urlpatterns = [

    path('/', views.account,name='accounts'),
    path('Donate',views.accountsDonte,name='Donate'),
    path('/signup',views.signup,name='signup'),
    path('/login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    path('/contribution',include('crowdfunding.urls'),name='contribution'),
    path('/plantTree',include('TreePlant.urls'),name='plantTree'),

]
