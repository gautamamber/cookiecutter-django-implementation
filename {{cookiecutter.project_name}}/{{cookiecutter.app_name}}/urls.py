from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [

	# Team URL
	path('', views.index, name = "index"),
	
]
