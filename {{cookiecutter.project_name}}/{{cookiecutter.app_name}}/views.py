from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "{{cookiecutter.app_name}}/index.html")