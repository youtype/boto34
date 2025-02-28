"""
Wrapper for boto3 Pricing service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pricing/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_pricing.client import PricingClient

from boto34.boto3.service_factory import ServiceFactory


class PricingService(ServiceFactory[PricingClient]):
    """
    Pricing service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pricing/)
    """
