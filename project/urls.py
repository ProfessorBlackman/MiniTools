from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Documentation.Swagger.urls')),
    path('user/', include('apps.Users.urls')),
    path('bitlink/', include('apps.BitLink.urls')),
]
