from apps.BitLink.models.urlmodel import UrlData
from apps.BitLink.utils.generate_url import urlgen


def update_url(data: dict) -> bool:
    if data["id"] is None:
        return False

    url_id = data['id']
    long_url = data.get('long_url')
    name = data.get('name')
    expires_at = data.get('expires_at')
    generate_new_slug = data.get('generate_new_slug')
    url_data = UrlData.objects.get(id=url_id)
    if long_url is not None:
        url_data.long_url = long_url
    if name is not None:
        url_data.name = name
    if expires_at is not None:
        url_data.expires_at = expires_at
    if generate_new_slug:
        short_url, slug = urlgen()
        url_data.short_url = short_url
        url_data.slug = slug
    url_data.save()
    return True
