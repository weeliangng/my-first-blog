from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta: #which model to build this form
		model = Post 
		fields = ('title','text',)