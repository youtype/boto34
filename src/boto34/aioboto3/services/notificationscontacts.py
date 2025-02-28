"""
Wrapper for aioboto3 UserNotificationsContacts service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_notificationscontacts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_notificationscontacts.client import UserNotificationsContactsClient

from boto34.aioboto3.service_factory import ServiceFactory


class UserNotificationsContactsService(ServiceFactory[UserNotificationsContactsClient]):
    """
    UserNotificationsContacts service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_notificationscontacts/)
    """
