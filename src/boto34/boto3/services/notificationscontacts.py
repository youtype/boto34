"""
Wrapper for boto3 UserNotificationsContacts service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_notificationscontacts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_notificationscontacts.client import UserNotificationsContactsClient

from boto34.boto3.service_factory import ServiceFactory


class UserNotificationsContactsService(ServiceFactory[UserNotificationsContactsClient]):
    """
    UserNotificationsContacts service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_notificationscontacts/)
    """
