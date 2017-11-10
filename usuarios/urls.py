from django.conf.urls import url
from usuarios import views

urlpatterns = [
	url(r'^usuario/new', views.new, name="newUser"),
	url(r'^usuario/login', views.user_login, name="login"),
	url(r'^usuario/arearestritapaciente', views.restricted_area_paciente, name="restricted_area_paciente"),
	url(r'^usuario/arearestritamedico', views.restricted_area_medico, name="restricted_area_medico"),
	url(r'^usuario/arearestritarecepcionista', views.restricted_area_recepcionista, name="restricted_area_recepcionista"),
]
