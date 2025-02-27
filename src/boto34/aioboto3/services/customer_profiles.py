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

from types_aiobotocore_customer_profiles.client import CustomerProfilesClient

from boto34.aioboto3.service_factory import ServiceFactory


class CustomerProfilesService(ServiceFactory[CustomerProfilesClient]):
    SERVICE_NAME = "customer-profiles"
    _SERVICE_PROP = "customer_profiles"
