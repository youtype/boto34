"""
Wrapper for aiobotocore LicenseManagerLinuxSubscriptions service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_linux_subscriptions/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_license_manager_linux_subscriptions.client import (
    LicenseManagerLinuxSubscriptionsClient,
)

from boto34.aiobotocore.service_factory import ServiceFactory


class LicenseManagerLinuxSubscriptionsService(
    ServiceFactory[LicenseManagerLinuxSubscriptionsClient]
):
    """
    LicenseManagerLinuxSubscriptions service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_linux_subscriptions/)
    """
