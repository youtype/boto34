"""
Wrapper for aiobotocore UserNotificationsContacts service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_notificationscontacts/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore UserNotificationsContacts client
    async with session.notificationscontacts.create_client() as notificationscontacts_client:
        notificationscontacts_client: (
            types_aiobotocore_notificationscontacts.client.UserNotificationsContactsClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_notificationscontacts.client import UserNotificationsContactsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class UserNotificationsContactsService(ServiceFactory[UserNotificationsContactsClient]):
    SERVICE_NAME = "notificationscontacts"
    _SERVICE_PROP = "notificationscontacts"
