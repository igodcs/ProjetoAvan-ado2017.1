from django.conf.urls import url
from servicos import views

urlpatterns = [
    url(r'^$', views.index, name="indexServicos"),
    
]
