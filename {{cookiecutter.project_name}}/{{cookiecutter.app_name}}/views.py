from django.shortcuts import render
from .models import Post
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
# Create your views here.

def index(request):
	return render(request, "{{cookiecutter.app_name}}/index.html")



class PostViewSet(ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    viewsets.GenericViewSet):
   
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolDetailSerializer