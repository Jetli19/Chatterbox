from django.shortcuts import render, HttpResponse
from chatterbox.models import Room, Message


# sem budeme pridavat

# API na hello

def hello(request, s): # request tu davam vzdy, s znaci ako string
    # return HttpResponse("HELLO WORLD!!!")
    return HttpResponse(f'HELLO, DEAR {s}!!! ')

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

#  pak sme prerobili na toto s pomocou uz search html, okial sa odkazujeme na context
def search(request, s):
    rooms = Room.objects.filter(name__contains=s)  # namiesto s budeme davat uz co sa bude hladat
    messages = Message.objects.filter(body__contains=s)  # namiesto s budeme davat uz co sa bude hladat

    context = {'rooms': rooms, 'messages': messages}
    return render(request, "chatterbox/search.html", context)



