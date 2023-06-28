from django.shortcuts import render, redirect
from .models import Room, Topic 
from .forms import RoomForm

#rooms= [
  #  {'id':1, 'name': "let learn python"},
    #{'id':2, 'name': "let learn Javascript"},
    #{#'id':3, 'name': "let learn PHP"},
    #{'id':4, 'name': "let learn HTML"},
#]
# Create your views here.
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
def updateRoom(request, pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
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
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=="POST":
        room.delete()
        return redirect('home')
    return render(request, 'baseApp/delete.html', {'obj': room})