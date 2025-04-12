from rest_framework import serializers
from .models import News, Course, Research

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = '__all__' 