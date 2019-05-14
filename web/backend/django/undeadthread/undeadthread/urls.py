"""undeadthread URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

import sys
from django.http import HttpResponse


ONE_UNDEAD_THREAD_FLAG = False


def undeadthread(request):
    import threading
    threading.Thread(target=loop, daemon=True).start()
    return HttpResponse("it works")


def loop():
    global ONE_UNDEAD_THREAD_FLAG
    from time import sleep, ctime
    if not ONE_UNDEAD_THREAD_FLAG:
        ONE_UNDEAD_THREAD_FLAG = True
    else:
        return

    while True:
        print(ctime(), file=sys.stderr)
        sleep(2)


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('undeadthread', undeadthread),
]
