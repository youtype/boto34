"""
Wrapper for boto3 CodeStarNotifications service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codestar_notifications/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 CodeStarNotifications client
    codestar_notifications_client = session.codestar_notifications.client()
    codestar_notifications_client: types_boto3_codestar_notifications.client.CodeStarNotificationsClient
    ```
"""

from __future__ import annotations

from types_boto3_codestar_notifications.client import CodeStarNotificationsClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_codestar_notifications.client import CodeStarNotificationsClient
except ImportError:
    CodeStarNotificationsClient = object  # type: ignore[misc,assignment]


class CodeStarNotificationsService(
    ServiceFactory[CodeStarNotificationsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codestar-notifications"
    _SERVICE_PROP = "codestar_notifications"
