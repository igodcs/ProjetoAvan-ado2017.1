from django.conf.urls import url
from sobre import views

urlpatterns = [
    url(r'^$', views.index, name="indexSobre"),
    
]
