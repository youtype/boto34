"""
Wrapper for boto3 LicenseManagerLinuxSubscriptions service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_license_manager_linux_subscriptions/)

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
    # Returns type annotated boto3 LicenseManagerLinuxSubscriptions client
    license_manager_linux_subscriptions_client = session.license_manager_linux_subscriptions.client()
    license_manager_linux_subscriptions_client: (
        types_boto3_license_manager_linux_subscriptions.client.LicenseManagerLinuxSubscriptionsClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_license_manager_linux_subscriptions.client import (
    LicenseManagerLinuxSubscriptionsClient,
)

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_license_manager_linux_subscriptions.client import (
        LicenseManagerLinuxSubscriptionsClient,
    )
except ImportError:
    LicenseManagerLinuxSubscriptionsClient = object  # type: ignore[misc,assignment]


class LicenseManagerLinuxSubscriptionsService(
    ServiceFactory[LicenseManagerLinuxSubscriptionsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "license-manager-linux-subscriptions"
    _SERVICE_PROP = "license_manager_linux_subscriptions"
