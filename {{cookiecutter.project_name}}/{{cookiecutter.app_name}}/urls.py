from django.conf.urls import include, url
from django.urls import path
from . import views 
from rest_framework_swagger.views import get_swagger_view
from .views import PostViewSet


schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [

	# Team URL

	path('schema/', schema_view),
	path('', views.index, name = "index"),
	path('post/', PostViewSet, name = "Post"),
	
]
