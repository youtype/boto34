"""
Wrapper for aioboto3 CodeStarNotifications service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codestar_notifications/)

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
    # Returns type annotated aioboto3 CodeStarNotifications client
    codestar_notifications_client = session.codestar_notifications.client()
    codestar_notifications_client: (
        types_aiobotocore_codestar_notifications.client.CodeStarNotificationsClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_codestar_notifications.client import CodeStarNotificationsClient
except ImportError:
    CodeStarNotificationsClient = object  # type: ignore[misc,assignment]


class CodeStarNotificationsService(
    ServiceFactory[CodeStarNotificationsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codestar-notifications"
    _SERVICE_PROP = "codestar_notifications"
