from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='news_articles')
    created_at = models.DateTimeField(auto_now_add=True)