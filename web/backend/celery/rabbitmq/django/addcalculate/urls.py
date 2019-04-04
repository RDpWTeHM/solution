
from django.contrib import admin
from django.urls import path
from django.urls import include

import add


urlpatterns = (
    path('admin/', admin.site.urls),

    path("", add.index, name="index"),
    path("tools/", include("tools.urls")),
)
