from django.shortcuts import render
from .models import Blogs

def allblogs(request):
    blogs = Blogs.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})