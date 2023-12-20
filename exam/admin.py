from django.contrib import admin
from .models import (
BSB,
CHSB,
Subject,
Grade
)

class BSBAdmin(admin.ModelAdmin):
    list_display = ("bsb_name", "subject", 'grade_number')
    list_filter = ("bsb_name", "subject", 'grade_number')
    search_fields = ("bsb_name", "subject.subject_name", 'grade_number.grade_num')
class CHSBAdmin(admin.ModelAdmin):
    list_display = ("chsb_name", "subject", 'grade_number')
    list_filter = ("chsb_name", "subject", 'grade_number')
    search_fields = ("chsb_name", "subject.subject_name", 'grade_number.grade_num')
# Register your models here.


admin.site.register(BSB, BSBAdmin)
admin.site.register(CHSB, CHSBAdmin)
admin.site.register(Subject)
admin.site.register(Grade)