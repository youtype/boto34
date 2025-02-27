"""
Wrapper for boto3 Pricing service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pricing/)

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
    # Returns type annotated boto3 Pricing client
    pricing_client = session.pricing.client()
    pricing_client: types_boto3_pricing.client.PricingClient
    ```
"""

from __future__ import annotations

from types_boto3_pricing.client import PricingClient

from boto34.boto3.service_factory import ServiceFactory


class PricingService(ServiceFactory[PricingClient]):
    SERVICE_NAME = "pricing"
    _SERVICE_PROP = "pricing"
