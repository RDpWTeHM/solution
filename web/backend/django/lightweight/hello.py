# hello.py

"""
Usage:
    $ python hello.py manage.py

"""

import sys
import os
from django.conf import settings
from django.urls import path

from django.http import HttpResponse


ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')


settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


def index(request):
    return HttpResponse("<h1>Hello World</h1>")


urlpatterns = (
    path("", index, name="index"),
)


if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
