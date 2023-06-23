from django.shortcuts import render

rooms= [
    {'id':1, 'name': "let learn python"},
    {'id':2, 'name': "let learn Javascript"},
    {'id':3, 'name': "let learn PHP"},
    {'id':4, 'name': "let learn HTML"},
]
# Create your views here.
def home(request):
    context ={'rooms':rooms}
    return render(request, "baseApp/home.html", context)
'''
room view
'''
def room(request, pk):
    room=None
    for i in rooms:
        if i['id'] == int(pk):
            room=i
    '''
    set context dictionary
    '''
    context={'room':room}
    return render(request, "baseApp/room.html", context)