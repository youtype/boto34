"""
Wrapper for aiobotocore LicenseManagerUserSubscriptions service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_license_manager_user_subscriptions.client import (
    LicenseManagerUserSubscriptionsClient,
)

from boto34.aiobotocore.service_factory import ServiceFactory


class LicenseManagerUserSubscriptionsService(ServiceFactory[LicenseManagerUserSubscriptionsClient]):
    """
    LicenseManagerUserSubscriptions service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager_user_subscriptions/)
    """
