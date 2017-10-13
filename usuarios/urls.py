from django.conf.urls import url
from usuarios import views

urlpatterns = [
    url(r'^$', views.index, name="indexUsuarios"),
    url(r'^usuarios/(?P<produto_id>[0-9]+)/', views.detalhes, name="detalhes"),

]
