from abc import ABC, abstractmethod

from django.db import transaction
from rest_framework.serializers import Serializer

from exceptions.InvalidInputsError import InvalidInputsError


class Service(Serializer, ABC):
    serializer_class: Serializer = None

    def service_clean(self):
        if not self.is_valid():
            raise InvalidInputsError(
                self.errors)

    @classmethod
    def execute(cls, inputs, files=None, **kwargs):
        instance = cls(inputs, files, **kwargs)
        instance.get_serializer()
        instance.service_clean()
        with transaction.atomic():
            return instance.process()

    def get_serializer(self):
        if self.serializer_class is None:
            raise NotImplementedError("serializer_class is not defined.")

    @abstractmethod
    def process(self, *args):
        """
        Contains the main methods for the service class
        args:
        self
        returns:
        void | None
        """
        raise NotImplementedError()

    @abstractmethod
    def post_process(self):
        """
        Contains implementations that should be run after the process method is executed
        args:
        self
        returns:
        void | None
        """
        pass
