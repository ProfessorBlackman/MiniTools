from django.contrib import admin
from django.urls import path, include

from apps.BitLink.views.redirect_url_view import RedirectUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', include('Documentation.urls')),
    path('user/', include('apps.Users.urls')),
    path('bitlink/', include('apps.BitLink.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('<str:slug>/', RedirectUrl.as_view(), name='url-redirect'),
    path('', include('django_prometheus.urls'))
]
