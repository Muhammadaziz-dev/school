from django.db import models
from users.models import CustomUser
from blog.models import Blog
from library.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    text = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    blog = models.ForeignKey(Blog, blank=True, on_delete=models.CASCADE, null=True, default="")
    book = models.ForeignKey(Book, blank=True, on_delete=models.CASCADE, null=True, default="")

    def __str__(self):
        return f"{self.text[:100]}... by {self.user.username}"
