"""
Wrapper for aioboto3 UserNotifications service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_notifications/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_notifications.client import UserNotificationsClient

from boto34.aioboto3.service_factory import ServiceFactory


class UserNotificationsService(ServiceFactory[UserNotificationsClient]):
    """
    UserNotifications service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_notifications/)
    """
