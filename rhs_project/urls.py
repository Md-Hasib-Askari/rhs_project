from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
   # admin
    path('admin/', admin.site.urls),
    path('accounts/profile/', views.admin_redirect),

    # Created Apps
    # path('', include('core.urls')),
    path('feed_posts/', include('feed_post.urls')),
    path('', include('webpages.urls')),

    # Extensions
    path('ckeditor', include('ckeditor_uploader.urls')),
]
