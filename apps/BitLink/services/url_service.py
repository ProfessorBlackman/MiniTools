from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from exceptions.base_custom_exception import BaseCustomException
from ..models.urlmodel import UrlData
from ..utils.generate_url import urlgen
from ..utils.update_url import update_url
from ...Users.models import User


class UrlService:
    def __init__(self, serializer=None):
        self.serializer_class = serializer

    def shorten_url(self, request) -> dict:
        data = request.data
        long = data.get('long_url')
        name = data.get('name')

        # user_email = request.user.email_address
        print(f"this is data: {data}")
        # print(f"this is user: {user_email}")

        serializer = self.serializer_class(data=data)
        print("I'm here")
        if not serializer.is_valid():
            print("serializer is not valid")
            raise BaseCustomException(
                message={'status': 'error', 'errors': 'Invalid name or url'},
                status=status.HTTP_406_NOT_ACCEPTABLE)
        print("now I'm here")
        try:
            print(f"this is long: {long}")
            is_entity_exist = UrlData.objects.filter(long_url=long).exists()
            print(f"this is long: {name}")
        except Exception as e:
            print(f"this is exist error: {e}")
            raise BaseCustomException(
                message={'status': 'error', 'errors': f"{e}"},
                status=status.HTTP_406_NOT_ACCEPTABLE)
        if is_entity_exist:  # see if any object with long as long_url exists
            print("Url already exists")
            raise BaseCustomException(
                message={'status': 'error', 'errors': 'url already exists'},
                status=status.HTTP_400_BAD_REQUEST)
        result_url, slug = urlgen()
        # try:
        #     user = User.objects.get(email_address=user_email)
        # except Exception as e:
        #     print(f"this is error: {e}")
        #     raise BaseCustomException(
        #         detail={'status': 'error', 'errors': e},
        #         code=status.HTTP_400_BAD_REQUEST)
        # print(f"this is user: {user.email_address}")
        try:
            new = UrlData.objects.create(name=name,
                                         long_url=long,
                                         short_url=result_url,
                                         slug=slug,
                                         related_user=request.user)
            print(f"new url: {new.short_url}")
            # new.full_clean()
            # new.save()
        except Exception as e:
            raise BaseCustomException(
                message={'status': 'error', 'errors': str(e)},
                status=status.HTTP_400_BAD_REQUEST)
        return {
            'status': 'success',
            'data': result_url
        }

    def update_url_data(self, request) -> dict:
        data = request.data
        print(f"this is data: {data}")
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            raise BaseCustomException(
                message={'status': 'error', 'errors': 'Invalid argument'},
                status=status.HTTP_400_BAD_REQUEST)

        is_saved_to_db = update_url(data=data)
        if is_saved_to_db is None:
            raise BaseCustomException(
                message={'status': 'error', 'error': 'Invalid id'},
                status=status.HTTP_400_BAD_REQUEST)

        return {
            'status': 'success',
            'errors': is_saved_to_db,
        }

    def read_all(self, request) -> dict:
        # user_email = request.user
        # try:
        #     user = get_object_or_404(User, email_address=user_email)
        # except User.DoesNotExist:
        #     raise BaseCustomException(
        #         message={'status': 'error', 'errors': "User does not exist"},
        #         status=status.HTTP_400_BAD_REQUEST)

        try:
            urls = get_list_or_404(UrlData, related_user=request.user)
        except Exception as e:
            raise BaseCustomException(
                message={'status': 'error', 'errors': e},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(urls, many=True)

        return {'status': 'success', 'data': serializer.data}

    def read_one(self, request, url_id: str) -> dict:
        try:
            url = UrlData.objects.get(id=url_id)
        except Exception as e:
            raise BaseCustomException(
                message={'status': 'error', 'errors': e},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(url)
        if url.related_user is not request.user:
            raise BaseCustomException(message={'status': 'error', 'errors': "url not related to user"},
                                      status=status.HTTP_403_FORBIDDEN)

        return {'status': 'success', 'data': serializer.data}

    def get_long_url(self, data: dict) -> dict:
        print(f"this is url: {data}")

        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            raise BaseCustomException(message={'status': 'error', 'errors': "Invalid url"},
                                      status=status.HTTP_406_NOT_ACCEPTABLE)
        try:
            url_details = get_object_or_404(UrlData, short_url=data["url"])
        except UrlData.DoesNotExist:
            raise BaseCustomException(
                message={'status': 'error', 'errors': "url does not exist"},
                status=status.HTTP_400_BAD_REQUEST)

        return {'status': 'success', 'data': url_details.long_url}

    def delete_url(self, url_id) -> dict:
        try:
            url_data = UrlData.objects.get(id=url_id)
            url_data.is_deleted = True
            url_data.save()
        except UrlData.DoesNotExist:
            raise BaseCustomException(
                message={'status': 'error', 'errors': "Url does not exist"},
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise BaseCustomException(
                message={'status': 'error', 'errors': e},
                status=status.HTTP_400_BAD_REQUEST)

        return {'status': 'success', 'data': 'url deleted'}
