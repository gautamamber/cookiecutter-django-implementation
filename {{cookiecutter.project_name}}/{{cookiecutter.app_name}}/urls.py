from django.conf.urls import include, url
from django.urls import path
from . import views 
from .views import PostViewSet


urlpatterns = [

	# Team URL
	path('', views.index, name = "index"),
	path('post/', PostViewSet, name = "Post"),
	
]
