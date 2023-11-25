from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    def __str__(self):
        return self.category_name
# Create your models here.
class Book(models.Model):
    name = models.CharField(blank=False, max_length=255)
    author = models.CharField(blank=False, max_length=255)
    isbn = models.CharField(max_length=13)
    description = models.TextField(default="", blank=False)
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)  # Slug maydonini o'zgartirdik

    def save(self, *args, **kwargs):
        # Agar slug bo'sh bo'lsa, avtomatik yaratamiz
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
