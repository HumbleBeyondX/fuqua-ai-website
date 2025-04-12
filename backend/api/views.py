from rest_framework import viewsets
from .models import News, Course, Research
from .serializers import NewsSerializer, CourseSerializer, ResearchSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('code')
    serializer_class = CourseSerializer

class ResearchViewSet(viewsets.ModelViewSet):
    queryset = Research.objects.all().order_by('-date')
    serializer_class = ResearchSerializer 