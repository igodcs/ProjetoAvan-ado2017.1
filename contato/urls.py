from django.conf.urls import url
from contato import views

urlpatterns = [
    url(r'^$', views.index, name="indexContato"),
    
]
