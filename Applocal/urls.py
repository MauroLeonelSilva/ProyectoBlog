from django.urls import path
from Applocal.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("post/", post, name="post"),
    path("miPerfil/", miPerfil, name="miPerfil"),
    path("leerPerfil/", leerPerfil, name="leerPerfil"),

    path("login/", login_request, name='login'),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("AgregarAvatar/", AgregarAvatar, name="AgregarAvatar"),
]