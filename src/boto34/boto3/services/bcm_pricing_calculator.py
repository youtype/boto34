"""
Wrapper for boto3 BillingandCostManagementPricingCalculator service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bcm_pricing_calculator/)

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
    # Returns type annotated boto3 BillingandCostManagementPricingCalculator client
    bcm_pricing_calculator_client = session.bcm_pricing_calculator.client()
    bcm_pricing_calculator_client: (
        types_boto3_bcm_pricing_calculator.client.BillingandCostManagementPricingCalculatorClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_bcm_pricing_calculator.client import (
    BillingandCostManagementPricingCalculatorClient,
)

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_bcm_pricing_calculator.client import (
        BillingandCostManagementPricingCalculatorClient,
    )
except ImportError:
    BillingandCostManagementPricingCalculatorClient = object  # type: ignore[misc,assignment]


class BillingandCostManagementPricingCalculatorService(
    ServiceFactory[BillingandCostManagementPricingCalculatorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bcm-pricing-calculator"
    _SERVICE_PROP = "bcm_pricing_calculator"
