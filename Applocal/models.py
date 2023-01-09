from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class contactomodel(models.Model):
    nombrecontacto = models.CharField(max_length=50)
    emailcontacto = models.EmailField()
    telefonocontacto = models.IntegerField()
    mensajecontacto = models.CharField(max_length=500)

    def __str__(self):

        return self.nombrecontacto+" "+self.emailcontacto+" "+str(self.telefonocontacto)+" "+self.mensajecontacto

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatares")
    user=models.ForeignKey(User, on_delete=models.CASCADE)  #con el foreignkey asocio la id entre modelos

    def __str__(self):
        return f"{self.user} - {self.imagen}"