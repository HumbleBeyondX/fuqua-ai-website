from django.contrib import admin
from .models import News, Course, Research

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'content')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'category', 'instructor', 'term')
    list_filter = ('category', 'term')
    search_fields = ('title', 'code', 'description')

@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'researcher', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description', 'researcher') 