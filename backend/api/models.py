from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=50)
    image_url = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)
    term = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code} - {self.title}"

class Research(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    researcher = models.CharField(max_length=100)
    date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title 