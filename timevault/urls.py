from django.contrib import admin
from django.urls import path, include  # ensure include is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('capsules.urls')),  # This line includes your app’s URLs
]