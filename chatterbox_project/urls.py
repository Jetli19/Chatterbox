"""chatterbox_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# sem budeme pridavat

from django.contrib import admin
from django.urls import path,include
import chatterbox.views


urlpatterns = [
    path('admin/', admin.site.urls),

    # chatterbox aplikace, ktore sme vytvorili/vytvarame my
    # path('cesta', <views>, name='name')
    path('', chatterbox.views.home, name='home'),
    path('hello/<s>', chatterbox.views.hello), # hlada v zlozke chatterbox/views a konkretnu funkciu/aplikaciu
    path('search/<s>', chatterbox.views.search),
    path('room/<str:pk>/', chatterbox.views.room, name="room"),
    path('rooms/', chatterbox.views.rooms, name='rooms'),

    # accounts aplikace
    path("accounts/", include("accounts.urls")), # vygeneruje signup
    path("accounts/", include("django.contrib.auth.urls")), #vsetky ostatne authorizacne urls

    #path("__reload__/", include("django_browser_reload.urls"))
]

