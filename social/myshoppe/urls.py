from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views as main

urlpatterns = [
    path('admin/', admin.site.urls),
    #Main URLS
    
    path('main/', include('main.urls')),
    
]


# urlpatterns += static(settings.STORAGE_URL,
#                       document_root=settings.STORAGE_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
