from django.db import models

# Create your models here.
class BLOG (models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    title=models.CharField(max_length=255)
    text=models.TextField()

    def __str__(self):
        return self.title
