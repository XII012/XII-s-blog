from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    users = User.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'users': users})
