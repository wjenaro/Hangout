from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #decorator 
from .models import Room, Topic, User
from .forms import RoomForm
from django.contrib.auth import authenticate, login, logout

#rooms= [
  #  {'id':1, 'name': "let learn python"},
    #{'id':2, 'name': "let learn Javascript"},
    #{#'id':3, 'name': "let learn PHP"},
    #{'id':4, 'name': "let learn HTML"},
#]
# Create your views here.
def loginPage(request):
    page="login"
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "User does not exit")
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username does not exist")

    context={'pag':page}
    return render(request, 'baseApp/login_register.html', context)
    '''
    logout method
    '''
def logoutUser(request):
    logout(request)
    return redirect('home')
'''
register 
'''
def registerPage(request):
    #page='register'
    return render(request, 'baseApp/login_register.html')

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    '''creating topic object .. get to query all columns from the Topic table
    '''
    topics=Topic.objects.all()
    '''Create model manager
    '''
    rooms=Room.objects.filter(topic__name__icontains=q)
    ''''''
    context ={'rooms':rooms, 'topics': topics}
    '''
    '''
    return render(request, "baseApp/home.html", context)
'''
room view
'''
def room(request, pk):
    room=Room.objects.get(id=pk)
  
    '''
    set context dictionary
    '''
    context={'room':room}
    return render(request, "baseApp/room.html", context)

@login_required(login_url="login") #this means that user cannot start creating rooms is not login 
def createRoom(request):
    form=RoomForm()
    if request.method=="POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={'form':form}
    return render(request, 'baseApp/room_form.html', context)
'''
updating 
'''
@login_required(login_url="login") 
def updateRoom(request, pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    '''
    Ensure only user can update'''
    if request.user!=room.user:
        return HttpResponse("You cannot update since you are not login")


    if request.method=="POST":
        form=RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request, 'baseApp/room_form.html', context)
'''
Delete
'''
@login_required(login_url="login") 
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=="POST":
        room.delete()
        return redirect('home')
    return render(request, 'baseApp/delete.html', {'obj': room})

