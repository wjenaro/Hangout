from django.contrib import admin

#register models
#start by importing the model
from .models import Room, Topic, Message
'''
kasi safi
'''
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

