from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class BSB(models.Model):
    file = models.FileField(upload_to="exam/bsb/", null=True)
    bsb_name = models.CharField(max_length=255)


    def __str__(self):
        return self.bsb_name
class CHSB(models.Model):
    file = models.FileField(upload_to="exam/chsb/", null=True)
    chsb_name = models.CharField(max_length=255)

    def __str__(self):
        return self.chsb_name


class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True, max_length=255)
    bsb = models.ManyToManyField(BSB, blank=False)
    chsb = models.ManyToManyField(CHSB, blank=False)

    def __str__(self):
        return self.subject_name

    def save(self, *args, **kwargs):
        if not self.slug:
            # Trim the title to a reasonable length before creating the slug
            trimmed_title = self.subject_name
            self.slug = slugify(trimmed_title)
        super().save(*args, **kwargs)

class Grade(models.Model):
    grade_number = models.PositiveSmallIntegerField(null=True, blank=False, unique=True,validators=[MinValueValidator(1), MaxValueValidator(11)])
    subjects = models.ManyToManyField(Subject, blank=False)

    def  __str__(self):
        return f"{self.grade_number}-sinf"