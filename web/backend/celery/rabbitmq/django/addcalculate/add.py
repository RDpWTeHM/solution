# add.py

"""
Usage:
    $ python add.py manage.py

"""
from __future__ import absolute_import, unicode_literals
from tools.celery import app as celery_app

import sys
import os

# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html', {})


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
