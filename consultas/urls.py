from django.conf.urls import url
from consultas import views

urlpatterns = [
    url(r'^$', views.index, name="indexConsultas"),
    url(r'^consultas/new/$', views.new, name="newConsulta"),
    url(r'^consultas/(?P<consulta_id>[0-9]+)/$', views.detalhes, name="detalhes"),
    url(r'^consultas/(?P<consulta_id>[0-9]+)/edit$', views.edit, name="edit"),
    url(r'^consultas/(?P<consulta_id>[0-9]+)/delete$', views.delete, name="delete"),
    url(r'^consultas/consultarestrita/$', views.consultarestrita, name="consultarestrita"),
    url(r'^consultas/consultarestritamedico/$', views.consultarestritamedico, name="consultarestritamedico"),
    url(r'^consultas/consultarestritapaciente/$', views.consultarestritapaciente, name="consultarestritapaciente"),

]
