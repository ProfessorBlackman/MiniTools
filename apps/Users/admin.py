from django.contrib import admin
from rest_framework_simplejwt import token_blacklist

from apps.Users.models.User import User


class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):  # type:ignore
    """_summary_"""

    def has_delete_permission(self, *args, **kwargs):
        return True  # or whatever logic you want


admin.site.unregister(token_blacklist.models.OutstandingToken)  # type: ignore
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)  # type: ignore

admin.site.register(
    (
        User,
    )
)
