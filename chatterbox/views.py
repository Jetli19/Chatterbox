from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from chatterbox.models import Room, Message



# sem budeme pridavat

# API na hello

def hello(request, s): # request tu davam vzdy, s znaci ako string
    # return HttpResponse("HELLO WORLD!!!")
    return HttpResponse(f'HELLO, DEAR {s}!!! ')


def home(request):
    rooms = Room.objects.all()  # najdeme všechny místnosti
    context = {'rooms': rooms}
    return render(request, 'chatterbox/home.html', context)


# API na search
# povodne bez templates
'''def search(request,s):
    rooms = Room.objects.filter(name__contains=s) # namiesto s budeme davat uz co sa bude hladat
    response = "Rooms: "
    for room in rooms:
        response += room.name + ", "
    # return HttpResponse(rooms)

    messages = Message.objects.filter(body__contains=s) # namiesto s budeme davat uz co sa bude hladat
    response += "<br>Messages: "
    for message in messages:
        response += message.body[0:10] + " ... , " # [0:10] zobrazi len zaciatok spravy a zbytok spravi ...


    return render(request, "chatterbox/search.html", context)'''

#  pak sme prerobili na toto s pomocou uz search html, odkial sa odkazujeme na context
@login_required
def search(request, s):
    rooms = Room.objects.filter(name__contains=s)  # namiesto 's' budeme davat uz co sa bude hladat
    messages = Message.objects.filter(body__contains=s)  # namiesto 's' budeme davat uz co sa bude hladat

    context = {'rooms': rooms, 'messages': messages} # vysledok=context a zobrazi rooms a messages s hladanym slovom
    return render(request, "chatterbox/search.html", context)

@login_required
def room(request, pk):
    room = Room.objects.get(id=pk) # najdem miestrost pomocou ID miestnosti resp PK
    messages = Message.objects.filter(room=pk) # zobrazi spravy v danej miestnosti

    context = {'room': room,'messages': messages}
    return render(request, "chatterbox/room.html", context)

@login_required # zakaze zobrazenie pre neprihlasenych users
def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'chatterbox/rooms.html', context)




