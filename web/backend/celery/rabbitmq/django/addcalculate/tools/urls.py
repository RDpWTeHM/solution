from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),

    path("add/", views.add_1),
    path("result/", views.result, name="add_result"),
]
