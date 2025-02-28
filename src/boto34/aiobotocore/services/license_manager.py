"""
Wrapper for aiobotocore LicenseManager service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_license_manager.client import LicenseManagerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class LicenseManagerService(ServiceFactory[LicenseManagerClient]):
    """
    LicenseManager service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_license_manager/)
    """
