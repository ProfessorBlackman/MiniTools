from django.urls import path

from apps.BitLink.views.shorten_url_view import ShortenUrl

urlpatterns = [
    path('shorten/', ShortenUrl.as_view(), name='token_refresh'),
]
