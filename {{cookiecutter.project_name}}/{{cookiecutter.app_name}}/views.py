from django.shortcuts import render
from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets
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
   
    queryset = Post.objects.all()
    serializer_class = PostSerializer