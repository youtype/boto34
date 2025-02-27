"""
Wrapper for aioboto3 UserNotificationsContacts service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_notificationscontacts/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 UserNotificationsContacts client
    notificationscontacts_client = session.notificationscontacts.client()
    notificationscontacts_client: (
        types_aiobotocore_notificationscontacts.client.UserNotificationsContactsClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_notificationscontacts.client import UserNotificationsContactsClient
except ImportError:
    UserNotificationsContactsClient = object  # type: ignore[misc,assignment]


class UserNotificationsContactsService(
    ServiceFactory[UserNotificationsContactsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "notificationscontacts"
    _SERVICE_PROP = "notificationscontacts"
