from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("django.contrib.auth.urls")),
    path("", include("library.urls", namespace="library")),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
