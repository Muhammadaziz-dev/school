from django.db import models

# Create your models here.
class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel/', default="")
    description = models.CharField(max_length=255, default="No description")
    created_at = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.description


