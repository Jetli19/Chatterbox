from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
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
    room = Room.objects.get(id=pk) # najde miestnost pomocou ID miestnosti resp PK
    messages = Message.objects.filter(room=pk) # zobrazi spravy v danej miestnosti

    # pokud zadame novou spravu, musim ju spracovat
    if request.method == 'POST': # ak odoslem spravu, pouzije sa prikaz POST z room.html
        # odosle sa sprava, kde bude prihlaseny user, v aktualnej roomke a telo textu
        body = request.POST.get ('body').strip() # osetri nam aby nesli odoslat prazdne spravy pripadne s medzernikom
        if len(body) > 0:
            message = Message.objects.create(
                user = request.user,
                room = room,
                body = body,
            )
        return HttpResponseRedirect(request.path_info) # refresh stranky, aby sa sprava zobrazila

    context = {'room': room,'messages': messages}
    return render(request, "chatterbox/room.html", context)

@login_required # zakaze zobrazenie pre neprihlasenych user
def rooms(request):
    rooms = Room.objects.all()

    context = {'rooms': rooms}
    return render(request, 'chatterbox/rooms.html', context)



@login_required
def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        descr = request.POST.get('descr').strip()
        if len(name) > 0 and len(descr) > 0:
            room = Room.objects.create(
                name=name,
                description=descr
            )

            return redirect('room', pk=room.id)

    return render(request, 'chatterbox/create_room.html')



