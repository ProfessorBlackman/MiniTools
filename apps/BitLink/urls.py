from django.urls import path, re_path

from apps.BitLink.serializers.get_all_urls import ListAllUrlsView
from apps.BitLink.views.get_long_url import GetLongUrlView
from apps.BitLink.views.url_view import Url
from apps.BitLink.views.url_details_view import UrlDetailsView

urlpatterns = [
    path('url/', Url.as_view(), name='shorten-url'),
    path('get-long/', GetLongUrlView.as_view(), name='url-info'),
    re_path(r'^url/(?P<url>\w+)/$', GetLongUrlView.as_view(), name='url-list'),
    path('urldetails/', UrlDetailsView.as_view(), name='url-details'),
    path('all/', ListAllUrlsView.as_view(), name='url-list')
]
