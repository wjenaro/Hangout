from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "baseApp/home.html")
'''
room view
'''
def room(request):
    return render(request, "baseApp/room.html")