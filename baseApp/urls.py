from django.urls import path
#import views
from . import views
'''
declare urlspatterns to handle urls requests for this app (BaseApp)
'''
urlpatterns=[
    path('', views.home, name="home"),
    path('/room', views.room, name="room"),
]