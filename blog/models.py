from django.db import models
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (
        ('Pub', 'Published'),
        ('Drf', 'Draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    datetime_creation = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    
    
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
