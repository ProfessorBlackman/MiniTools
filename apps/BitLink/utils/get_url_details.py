from rest_framework import status

from apps.BitLink.models.urlmodel import UrlData
from exceptions.base_custom_exception import BaseCustomException


def get_url_details(url: UrlData):
    try:
        short_url = url.short_url
        long_url = url.long_url
        slug = url.slug
        name = url.name
        no_of_uses = url.no_of_uses
        timestamp = url.timestamp
        date_created = url.date_created.strftime('%Y-%m-%d %H:%M:%S')
        date_modified = url.date_modified.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise BaseCustomException(
            message=e, status=status.HTTP_404_NOT_FOUND
        )

    return {"short_url": short_url,
            "long_url": long_url,
            "slug": slug,
            "name": name,
            "no_of_uses": no_of_uses,
            "timestamp": timestamp,
            "date_created": date_created,
            "date_modified": date_modified}
