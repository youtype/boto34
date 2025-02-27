"""
Wrapper for aiobotocore CodeStarNotifications service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_notifications/)

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
    # Returns type annotated aiobotocore CodeStarNotifications client
    async with session.codestar_notifications.create_client() as codestar_notifications_client:
        codestar_notifications_client: (
            types_aiobotocore_codestar_notifications.client.CodeStarNotificationsClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_codestar_notifications.client import CodeStarNotificationsClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_codestar_notifications.client import CodeStarNotificationsClient
except ImportError:
    CodeStarNotificationsClient = object  # type: ignore[misc,assignment]


class CodeStarNotificationsService(
    ServiceFactory[CodeStarNotificationsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codestar-notifications"
    _SERVICE_PROP = "codestar_notifications"
