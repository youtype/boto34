"""
Wrapper for aioboto3 CustomerProfiles service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_customer_profiles/)

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
    # Returns type annotated aioboto3 CustomerProfiles client
    customer_profiles_client = session.customer_profiles.client()
    customer_profiles_client: types_aiobotocore_customer_profiles.client.CustomerProfilesClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_customer_profiles.client import CustomerProfilesClient
except ImportError:
    CustomerProfilesClient = object  # type: ignore[misc,assignment]


class CustomerProfilesService(
    ServiceFactory[CustomerProfilesClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "customer-profiles"
    _SERVICE_PROP = "customer_profiles"
