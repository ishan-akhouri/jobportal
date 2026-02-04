"""config URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views  # Import the views directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),  # Direct home route
    path('users/', include('users.urls')),    # Other user URLs will be under /users/
    path('jobs/', include('jobs.urls')),      # Job URLs under /jobs/
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
