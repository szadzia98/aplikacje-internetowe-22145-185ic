from django.urls import path

from . import views
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]
router = DefaultRouter()
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls