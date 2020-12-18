from django.urls import path, include

from . import views
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('index/', views.index, name='index')
]
