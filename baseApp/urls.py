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
]