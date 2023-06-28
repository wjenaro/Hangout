from django.urls import path
#import views
from . import views
'''
declare urlspatterns to handle urls requests for this app (BaseApp)
'''
urlpatterns=[
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]