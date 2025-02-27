"""
Wrapper for aioboto3 LicenseManagerUserSubscriptions service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_license_manager_user_subscriptions/)

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
    # Returns type annotated aioboto3 LicenseManagerUserSubscriptions client
    license_manager_user_subscriptions_client = session.license_manager_user_subscriptions.client()
    license_manager_user_subscriptions_client: types_aiobotocore_license_manager_user_subscriptions.client.LicenseManagerUserSubscriptionsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_license_manager_user_subscriptions.client import (
    LicenseManagerUserSubscriptionsClient,
)

from boto34.aioboto3.service_factory import ServiceFactory


class LicenseManagerUserSubscriptionsService(ServiceFactory[LicenseManagerUserSubscriptionsClient]):
    SERVICE_NAME = "license-manager-user-subscriptions"
    _SERVICE_PROP = "license_manager_user_subscriptions"
