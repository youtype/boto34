"""
Wrapper for boto3 LicenseManagerUserSubscriptions service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_license_manager_user_subscriptions/)

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
    # Returns type annotated boto3 LicenseManagerUserSubscriptions client
    license_manager_user_subscriptions_client = session.license_manager_user_subscriptions.client()
    license_manager_user_subscriptions_client: (
        types_boto3_license_manager_user_subscriptions.client.LicenseManagerUserSubscriptionsClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_license_manager_user_subscriptions.client import (
    LicenseManagerUserSubscriptionsClient,
)

from boto34.boto3.service_factory import ServiceFactory


class LicenseManagerUserSubscriptionsService(ServiceFactory[LicenseManagerUserSubscriptionsClient]):
    SERVICE_NAME = "license-manager-user-subscriptions"
    _SERVICE_PROP = "license_manager_user_subscriptions"
