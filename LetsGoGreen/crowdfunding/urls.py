from django.contrib import admin
from django.urls import path
from crowdfunding import views

urlpatterns = [

    # path('', views.index),
    path('',views.contribution,name='contribution'),
    path('/updateUserProfile',views.updateUserProfile,name='updateUserProfile'),
    path('/userInfo',views.userInfo,name='userInfo'),
    path('/paymentGateways',views.paymentGateways,name='paymentGateways'),
    path('/sapling',views.sapling,name='sapling'),
    path('/catalogtree',views.catalogtree,name='catalogtree'),
    path('/catalogtreemore/<int:id>',views.catalogtreemore,name='catalogtreemore'),
    path('/treeanalysis',views.treeanalysis,name='treeanalysis'),

    path('addSapling',views.addSapling,name="addSapling"),


]
