from django.contrib import admin

from carousel.models import Carousel


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', "description", "created_at")
# Register your models here.
admin.site.register(Carousel, CarouselAdmin)