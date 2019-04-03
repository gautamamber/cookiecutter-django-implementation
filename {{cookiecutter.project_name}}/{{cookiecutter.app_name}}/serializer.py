from .models import Post
from rest_framework import serialzers



class PostSerializer(serialzers.ModelSerialzer):
	class Meta:
		model = Post
		fields = "__all__"