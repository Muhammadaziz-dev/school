from django.db import models
from django.utils.text import slugify
from django.utils import timezone  # Add this line

from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = CKEditor5Field("Text", config_name='extends')
    slug = models.SlugField(blank=True, unique=True, max_length=255)  # Slug maydonini o'zgartirdik
    video = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blogs/images/", blank=False, default="")
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Trim the title to a reasonable length before creating the slug
            trimmed_title = self.title[:50]
            self.slug = slugify(trimmed_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
