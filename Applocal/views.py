from django.shortcuts import render
from .models import *
from Applocal.forms import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required #vistas para funciones


# Create your views here.


def inicio(request):
    if request.user.is_authenticated:
        return render (request, "inicio.html", {"imagen":obtenerAvatar(request)})
    else:
        return render (request, "inicio.html")


def about(request):
    if request.user.is_authenticated:
        return render (request, "about.html", {"imagen":obtenerAvatar(request)})
    else:
        return render (request, "about.html")


@login_required
def contact(request):
    
    if request.method=="POST":
        form=ContactoForm(request.POST)
    
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombreform=informacion["nombre"]
            emailform=informacion["email"]
            numeroform=informacion["numero_telefono"]
            mensajeform=informacion["mensaje"]

            contactoguardado=contactomodel(nombrecontacto=nombreform, emailcontacto=emailform, telefonocontacto=numeroform,  mensajecontacto=mensajeform)
            contactoguardado.save()
            return render (request, "inicio.html", {"imagen":obtenerAvatar(request)})
        else:
            return render (request, "contact.html", {"form": formulario, "imagen":obtenerAvatar(request)})
        
    else:
        formulario=ContactoForm()

    return render (request, "contact.html", {"form": formulario, "imagen":obtenerAvatar(request)})



def post(request):
    if request.user.is_authenticated:
        return render (request, "post.html", {"imagen":obtenerAvatar(request)})
    else:
        return render (request, "post.html")

#----------seccion Login ---------

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "login.html", {"mensaje":"usuario o contraseña incorrectos", "form":form})
    else:
        form = AuthenticationForm()
    return render (request, "login.html", {"form":form})

def register(request):

    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save() 
                                                           
            return render(request, "login.html", {"mensaje":f"usuario {username} creado correctamente"})
        else:
            return render(request, "register.html", {"form":form, "mensaje":"Error al crear el usuario"})


    else:
        form=RegistroUsuarioForm()
    return render(request, "register.html", {"form":form})



    #--------------Edición de usuario------------------

@login_required
def editarPerfil(request):

    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "inicio.html", {"mensaje": "perfil editado correctamente", "imagen":obtenerAvatar(request)})
        else:
            return render(request, "inicio.html", {"form":form, "mensaje":"Error al editar el perfil", "imagen":obtenerAvatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "editarUsuario.html", {"form":form, "imagen":obtenerAvatar(request)})

@login_required
def AgregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "inicio.html", {"mensaje":"Avatar agregador correctamente", "imagen":obtenerAvatar(request)})
        else:
            return render(request, "AgregarAvatar.html", {"formulario":form, "usuario": request.user, "imagen":obtenerAvatar(request)})
    else:
        form=AvatarForm()
        return render(request, "AgregarAvatar.html", {"formulario":form, "usuario": request.user, "imagen":obtenerAvatar(request)})

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/imagen_pordefecto.jpg"
    return imagen

