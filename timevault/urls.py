from django.contrib import admin
from django.urls import path, include  # ensure include is imported
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('capsules.urls')),  # This line includes your app’s URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)