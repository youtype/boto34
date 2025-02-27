"""
Wrapper for aioboto3 UserNotifications service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_notifications/)

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
    # Returns type annotated aioboto3 UserNotifications client
    notifications_client = session.notifications.client()
    notifications_client: types_aiobotocore_notifications.client.UserNotificationsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_notifications.client import UserNotificationsClient
except ImportError:
    UserNotificationsClient = object  # type: ignore[misc,assignment]


class UserNotificationsService(
    ServiceFactory[UserNotificationsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "notifications"
    _SERVICE_PROP = "notifications"
