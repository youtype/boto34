"""
Wrapper for boto3 UserNotificationsContacts service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_notificationscontacts/)

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
    # Returns type annotated boto3 UserNotificationsContacts client
    notificationscontacts_client = session.notificationscontacts.client()
    notificationscontacts_client: (
        types_boto3_notificationscontacts.client.UserNotificationsContactsClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_notificationscontacts.client import UserNotificationsContactsClient

from boto34.boto3.service_factory import ServiceFactory


class UserNotificationsContactsService(ServiceFactory[UserNotificationsContactsClient]):
    SERVICE_NAME = "notificationscontacts"
    _SERVICE_PROP = "notificationscontacts"
