from django.conf.urls import url
from cadastro import views

urlpatterns = [
    url(r'^$', views.index, name="indexCadastro"),
    url(r'^usuario/(?P<usuario_id>[1]+)/', views.detail, name="detail"),
]
