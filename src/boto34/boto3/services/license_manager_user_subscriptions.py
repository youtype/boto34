"""
Wrapper for boto3 LicenseManagerUserSubscriptions service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_license_manager_user_subscriptions/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_license_manager_user_subscriptions.client import (
    LicenseManagerUserSubscriptionsClient,
)

from boto34.boto3.service_factory import ServiceFactory


class LicenseManagerUserSubscriptionsService(ServiceFactory[LicenseManagerUserSubscriptionsClient]):
    """
    LicenseManagerUserSubscriptions service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_license_manager_user_subscriptions/)
    """
