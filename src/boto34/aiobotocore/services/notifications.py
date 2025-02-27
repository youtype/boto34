"""
Wrapper for aiobotocore UserNotifications service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_notifications/)

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
    # Returns type annotated aiobotocore UserNotifications client
    async with session.notifications.create_client() as notifications_client:
        notifications_client: types_aiobotocore_notifications.client.UserNotificationsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_notifications.client import UserNotificationsClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_notifications.client import UserNotificationsClient
except ImportError:
    UserNotificationsClient = object  # type: ignore[misc,assignment]


class UserNotificationsService(
    ServiceFactory[UserNotificationsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "notifications"
    _SERVICE_PROP = "notifications"
