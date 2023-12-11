from django.db import models
from django.template.defaultfilters import default
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name
# Create your models here.
class Book(models.Model):
    name = models.CharField(blank=False, max_length=255, default="")
    author = models.CharField(blank=False, max_length=255)
    isbn = models.CharField(max_length=13)
    description = models.TextField(default="", blank=False)
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)  # Slug maydonini o'zgartirdik
    cover_image = models.ImageField(upload_to="library/cover_images/", default="")
    book_file = models.FileField(upload_to="library/book_files", default="")


    def save(self, *args, **kwargs):
        # Agar slug bo'sh bo'lsa, avtomatik yaratamiz
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
