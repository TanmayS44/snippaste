from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_snippet, name="create_snippet"),
    path("view/<int:snippet_id>/", views.view_snippet, name="view_snippet"),
]
