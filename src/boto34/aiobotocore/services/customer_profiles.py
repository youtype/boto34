"""
Wrapper for aiobotocore CustomerProfiles service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_customer_profiles.client import CustomerProfilesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CustomerProfilesService(ServiceFactory[CustomerProfilesClient]):
    """
    CustomerProfiles service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/)
    """
