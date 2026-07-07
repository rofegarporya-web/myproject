from django.db import models
from django.db.models import CASCADE

class Continent(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='cover/')

    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'images')
    img = models.ImageField(upload_to='posts/')
    def __str__(self):
        return f"Image {self.id}"
