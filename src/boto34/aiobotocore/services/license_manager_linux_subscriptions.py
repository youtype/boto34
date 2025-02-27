"""
Wrapper for aiobotocore LicenseManagerLinuxSubscriptions service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_linux_subscriptions/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore LicenseManagerLinuxSubscriptions client
    async with (
        session.license_manager_linux_subscriptions.create_client()
    ) as license_manager_linux_subscriptions_client:
        license_manager_linux_subscriptions_client: types_aiobotocore_license_manager_linux_subscriptions.client.LicenseManagerLinuxSubscriptionsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_license_manager_linux_subscriptions.client import (
    LicenseManagerLinuxSubscriptionsClient,
)

from boto34.aiobotocore.service_factory import ServiceFactory


class LicenseManagerLinuxSubscriptionsService(
    ServiceFactory[LicenseManagerLinuxSubscriptionsClient]
):
    SERVICE_NAME = "license-manager-linux-subscriptions"
    _SERVICE_PROP = "license_manager_linux_subscriptions"
