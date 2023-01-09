from django.shortcuts import render

from django.views.generic import DetailView

from .models import CanalMensaje, Canal
from django.http import Http404

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import FormMensajes
from django.views.generic.edit import FormMixin

from django.views.generic import View

from Applocal.models import Avatar

from django.contrib.auth import get_user_model






class Inbox(View):
	def get(self, request):
		
		lista=Avatar.objects.filter(user=request.user)
		if len(lista)!=0:
			imagen=lista[0].imagen.url
		else:
			imagen=None

		inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])


		context = {

			"imagen":imagen,
			"inbox":inbox,
	
		}
			

		return render(request, 'inbox.html', context)


class CanalFormMixin(FormMixin):
	form_class =FormMensajes

	def get_success_url(self):
		return self.request.path

	def post(self, request, *args, **kwargs):

		if not request.user.is_authenticated:
			raise PermissionDenied

		form = self.get_form()
		if form.is_valid():
			canal = self.get_object()
			usuario = self.request.user 
			mensaje = form.cleaned_data.get("mensaje")
			canal_obj = CanalMensaje.objects.create(canal=canal, usuario=usuario, texto=mensaje)
			return super().form_valid(form)
		else:
			return super().form_invalid(form)
			


class CanalDetailView(LoginRequiredMixin, CanalFormMixin, DetailView):
	template_name="canal_detail.html"
	queryset = Canal.objects.all()
	

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)


		obj = context['object']
		print(obj)

		context['si_canal_miembro'] = self.request.user in obj.usuarios.all()
		return context
	
	

class DerailMs(LoginRequiredMixin, CanalFormMixin, DetailView):  #Detail de mensajes

	template_name="canal_detail.html"

	def get_object(self, *args, **kwargs):

		username = self.kwargs.get("username")
		mi_username = self.request.user.username
		canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

		if username == mi_username:
			mi_canal, _ = Canal.objects.obtener_o_crear_canal_usuario_actual(self.request.user)

			return mi_canal

		if canal == None:
			raise Http404

		return canal


	#para crear un canal nuevo necesito poner el request: http://127.0.0.1:8000/AppMensajes/MensajeDirecto/Paco

	#necesito un formulario que me muestre los nombres de que esten logeados
	#cuando elija uno puedo clickear sobre el y me crea el chat devolviendo "Appmensajes/MensajeDirecto/Paco"


def busquedaUsuarios(request):

		User = get_user_model()
		usuarios = User.objects.all()
		
		return render(request, "busquedaUsuarios.html", {"usuarios":usuarios})




