from django.urls import path, include, re_path

from .views import DerailMs, CanalDetailView, Inbox, busquedaUsuarios
	
#"c66cde68-bf1a-4965-9be4-09438daf0482" este es un ejemplo de un codigo de id que se generan automaticamente, siempre tienen la misma cantidad de caracteres entre guiones
#el codigo de abajo es una manera de recuperar los codigos id de los canales de mensajeria, [a-f0-9]{8}, indica que hay 8 caracteres entre letras y numeros, el -? indica que hay un guion y que si se quita alguno de los numeros o letras de cada cadena no se rompe la pagina solo nos tira error de que no existe ese canal
UUID_CANAL_REGEX = r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'


urlpatterns=[

	re_path(UUID_CANAL_REGEX, CanalDetailView.as_view()),
	
	path("MensajeDirecto/<str:username>", DerailMs.as_view(), name="detailms"),
    path("Applocal/", include("Applocal.urls")),
	path("busquedaUsuarios/", busquedaUsuarios, name="busquedausuarios"),
	
	path("inbox/", Inbox.as_view(), name="inbox"),
	



]