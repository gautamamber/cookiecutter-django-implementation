from django.conf.urls import include, url
from django.urls import path
from . import views 
from .views import PostViewSet

schema_view = get_swagger_view(title='API')
urlpatterns = [

	# Team URL
	path('', views.index, name = "index"),
	path('post/', PostViewSet, name = "Post"),
	
]
