from django.contrib import admin
from django.urls import path,include

from accountsCrowd import views

urlpatterns = [

    path('/', views.accountsCrowds,name='Donate'),

    path('/cSignup',views.cSignup,name='cSignup'),
    path('/cLogin',views.cLogin,name='cLogin'),
    path('/contribution',include('crowdfunding.urls'),name='contribution')
    # path('/signup',views.signup,name='signup'),
    # path('/login',views.login,name='login'),
    # path('logout',views.logout,name='logout'),

    # path('/contribution',include('crowdfunding.urls'),name='contribution'),
    # path('/plantTree',include('TreePlant.urls'),name='plantTree'),

]
