from django.shortcuts import render

from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(status='P')
    return render(request, 'blog/post_list.html', context={
        'posts':posts,
    })
