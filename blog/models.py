from django.db import models
from django.utils.text import slugify

from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = CKEditor5Field("Text", config_name='extends')
    slug = models.SlugField(blank=True, unique=True)  # Slug maydonini o'zgartirdik
    video = models.FileField(upload_to="blogs/videos/", default="")
    image = models.ImageField(upload_to="blogs/images/", blank=False, default="")

    def save(self, *args, **kwargs):
        # Agar slug bo'sh bo'lsa, avtomatik yaratamiz
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
