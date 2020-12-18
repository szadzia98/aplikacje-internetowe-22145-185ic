from django.shortcuts import render

from rest_framework import generics, viewsets

from .models import Post
from .serializers import PostSerializer
from datetime import datetime
# Create your views here.
'''
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''


def index(request): 
    visits = int(request.COOKIES.get('visits', '1'))

    reset_last_visit_time = False
    response = render(request, 'index.html', {'visits':visits})
    if 'last_visit' in request.COOKIES: 
        last_visit = request.COOKIES['last_visit'] 
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S") 
        if (datetime.now() - last_visit_time).total_seconds() > 0.5:
            visits = visits + 1 
            reset_last_visit_time = True
    else: 
        reset_last_visit_time = True

        
        response = render(request, 'index.html', {'visits':visits})

    if reset_last_visit_time:
        response.set_cookie('last_visit', datetime.now())
        response.set_cookie('visits', visits) 
    return response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer