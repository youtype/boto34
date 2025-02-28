"""
Wrapper for boto3 UserNotifications service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_notifications/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_notifications.client import UserNotificationsClient

from boto34.boto3.service_factory import ServiceFactory


class UserNotificationsService(ServiceFactory[UserNotificationsClient]):
    """
    UserNotifications service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_notifications/)
    """
