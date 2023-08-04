from django.urls import path

from apps.BitLink.views.get_long_url import GetLongUrlView
from apps.BitLink.views.shorten_url_view import ShortenUrl
from apps.BitLink.views.url_details_view import UrlDetailsView

urlpatterns = [
    path('shorten/', ShortenUrl.as_view(), name='shorten-url'),
    path('get-long/', GetLongUrlView.as_view(), name='url-info'),
    path('urldetails/', UrlDetailsView.as_view(), name='url-details')
]
