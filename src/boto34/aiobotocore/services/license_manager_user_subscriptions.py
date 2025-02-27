"""
Wrapper for aiobotocore LicenseManagerUserSubscriptions service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/)

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
    # Returns type annotated aiobotocore LicenseManagerUserSubscriptions client
    async with (
        session.license_manager_user_subscriptions.create_client()
    ) as license_manager_user_subscriptions_client:
        license_manager_user_subscriptions_client: types_aiobotocore_license_manager_user_subscriptions.client.LicenseManagerUserSubscriptionsClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_license_manager_user_subscriptions.client import (
        LicenseManagerUserSubscriptionsClient,
    )
except ImportError:
    LicenseManagerUserSubscriptionsClient = object  # type: ignore[misc,assignment]


class LicenseManagerUserSubscriptionsService(
    ServiceFactory[LicenseManagerUserSubscriptionsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "license-manager-user-subscriptions"
    _SERVICE_PROP = "license_manager_user_subscriptions"
