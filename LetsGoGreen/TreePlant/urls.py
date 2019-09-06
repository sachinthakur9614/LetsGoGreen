from django.contrib import admin
from django.urls import path
from TreePlant import views

urlpatterns = [

    path('', views.plantTree,name='plantTree'),
    path('/userProfile',views.userProfile,name='userProfile'),
    path('/editProfile',views.editProfile,name='edituserProfile'),
    path('/userSuggestion',views.userSuggestion,name='userSuggestion'),
    path('/deleteAccount',views.deleteAccount,name='deleteAccount'),
    path('/deletedAccount',views.deletedAccount,name='deletedAccount'),
    path('/treeCatalog',views.treeCatalog,name='treecatalog'),
    path('/treeCatalogInfo/<int:id>',views.treeCatalogInfo,name='treecataloginfo'),
    path('/treeImages',views.treeImages,name='treeImages'),
    path('/treeImagesUpload',views.treeImagesUpload,name='treeImagesUpload'),
    path('/treeCount',views.treeCount,name='treeCount'),
    path('/treeLocation',views.treeLocation,name='treeLocation'),
    path('/treeLocationForm',views.treeLocationForm,name='treeLocationForm'),
    path('/editeTreeGrowth',views.editeTreeGrowth,name='editeTreeGrowth'),
    path('/placeAvailable',views.placeAvailable,name='placeAvailable'),
    path('/video',views.vedio,name='video'),



    
    
]

