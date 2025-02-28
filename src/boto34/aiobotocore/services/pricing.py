"""
Wrapper for aiobotocore Pricing service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pricing/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pricing.client import PricingClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PricingService(ServiceFactory[PricingClient]):
    """
    Pricing service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pricing/)
    """
