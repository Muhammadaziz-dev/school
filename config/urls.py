from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view
# from django.conf.urls import url
schema_view = get_swagger_view(title='Your API')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", include('api.urls')),
    path('library/', include('library.urls')),
    path("api/", include("api.urls")),
    path("blogs/", include("blog.urls")),
    path("comments/", include("comments.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path("carousel/", include("carousel.urls")),
    path("exam/", include("exam.urls")),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)