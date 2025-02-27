"""
Wrapper for aioboto3 BillingandCostManagementPricingCalculator service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bcm_pricing_calculator/)

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
    # Returns type annotated aioboto3 BillingandCostManagementPricingCalculator client
    bcm_pricing_calculator_client = session.bcm_pricing_calculator.client()
    bcm_pricing_calculator_client: (
        types_aiobotocore_bcm_pricing_calculator.client.BillingandCostManagementPricingCalculatorClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_bcm_pricing_calculator.client import (
        BillingandCostManagementPricingCalculatorClient,
    )
except ImportError:
    BillingandCostManagementPricingCalculatorClient = object  # type: ignore[misc,assignment]


class BillingandCostManagementPricingCalculatorService(
    ServiceFactory[BillingandCostManagementPricingCalculatorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bcm-pricing-calculator"
    _SERVICE_PROP = "bcm_pricing_calculator"
