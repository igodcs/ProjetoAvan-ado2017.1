from django.conf.urls import url
from usuarios import views

urlpatterns = [
    url(r'^$', views.index, name="indexUsuarios"),
    url(r'^usuarios/new', views.new, name="new"),
    url(r'^usuarios/(?P<usuario_id>[0-9]+)/', views.detalhes, name="detalhes"),
    url(r'^usuarios/(?P<usuario_id>[0-9]+)/edit', views.edit, name="edit"),
    url(r'^usuarios/(?P<usuario_id>[0-9]+)/delete', views.delete, name="delete"),
    

]
