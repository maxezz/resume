from django.shortcuts import render
from .models import BLOG

# Create your views here.
def blog (request):
    blogs=BLOG.objects
    return render (request ,'blog/blog.html',{'blogs':blogs})
