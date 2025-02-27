"""
Wrapper for aioboto3 LicenseManagerLinuxSubscriptions service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_license_manager_linux_subscriptions/)

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
    # Returns type annotated aioboto3 LicenseManagerLinuxSubscriptions client
    license_manager_linux_subscriptions_client = session.license_manager_linux_subscriptions.client()
    license_manager_linux_subscriptions_client: types_aiobotocore_license_manager_linux_subscriptions.client.LicenseManagerLinuxSubscriptionsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_license_manager_linux_subscriptions.client import (
    LicenseManagerLinuxSubscriptionsClient,
)

from boto34.aioboto3.service_factory import ServiceFactory


class LicenseManagerLinuxSubscriptionsService(
    ServiceFactory[LicenseManagerLinuxSubscriptionsClient]
):
    SERVICE_NAME = "license-manager-linux-subscriptions"
    _SERVICE_PROP = "license_manager_linux_subscriptions"
