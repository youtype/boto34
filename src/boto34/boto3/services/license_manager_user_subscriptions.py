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

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_license_manager_user_subscriptions.client import (
        LicenseManagerUserSubscriptionsClient,
    )
except ImportError:
    LicenseManagerUserSubscriptionsClient = object  # type: ignore[misc,assignment]


class LicenseManagerUserSubscriptionsService(
    ServiceFactory[LicenseManagerUserSubscriptionsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "license-manager-user-subscriptions"
    _SERVICE_PROP = "license_manager_user_subscriptions"
