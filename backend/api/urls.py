from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .views import NewsViewSet, CourseViewSet, ResearchViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'research', ResearchViewSet)

# API root view
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'news': reverse('news-list', request=request, format=format),
        'courses': reverse('course-list', request=request, format=format),
        'research': reverse('research-list', request=request, format=format),
    })

urlpatterns = [
    path('', include(router.urls)),
] 