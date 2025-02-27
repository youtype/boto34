"""
Wrapper for aiobotocore CustomerProfiles service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/)

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
    # Returns type annotated aiobotocore CustomerProfiles client
    async with session.customer_profiles.create_client() as customer_profiles_client:
        customer_profiles_client: types_aiobotocore_customer_profiles.client.CustomerProfilesClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_customer_profiles.client import CustomerProfilesClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CustomerProfilesService(ServiceFactory[CustomerProfilesClient]):
    SERVICE_NAME = "customer-profiles"
    _SERVICE_PROP = "customer_profiles"
