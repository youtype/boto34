"""
Wrapper for boto3 LicenseManagerLinuxSubscriptions service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_license_manager_linux_subscriptions/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_license_manager_linux_subscriptions.client import (
    LicenseManagerLinuxSubscriptionsClient,
)

from boto34.boto3.service_factory import ServiceFactory


class LicenseManagerLinuxSubscriptionsService(
    ServiceFactory[LicenseManagerLinuxSubscriptionsClient]
):
    """
    LicenseManagerLinuxSubscriptions service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_license_manager_linux_subscriptions/)
    """
