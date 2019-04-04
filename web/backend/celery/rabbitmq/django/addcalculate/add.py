# add.py

"""
Usage:
    $ python add.py manage.py

"""

import sys
import os

from django.urls import path

# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html', {})


urlpatterns = (
    path("", index, name="index"),
)


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
