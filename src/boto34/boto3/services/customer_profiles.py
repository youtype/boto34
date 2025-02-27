"""
Wrapper for boto3 CustomerProfiles service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_customer_profiles/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 CustomerProfiles client
    customer_profiles_client = session.customer_profiles.client()
    customer_profiles_client: types_boto3_customer_profiles.client.CustomerProfilesClient
    ```
"""

from __future__ import annotations

from types_boto3_customer_profiles.client import CustomerProfilesClient

from boto34.boto3.service_factory import ServiceFactory


class CustomerProfilesService(ServiceFactory[CustomerProfilesClient]):
    SERVICE_NAME = "customer-profiles"
    _SERVICE_PROP = "customer_profiles"
