from django.contrib import admin
from .models import (
BSB,
CHSB,
Subject,
Grade
)
# Register your models here.
admin.site.register(BSB)
admin.site.register(CHSB)
admin.site.register(Subject)
admin.site.register(Grade)