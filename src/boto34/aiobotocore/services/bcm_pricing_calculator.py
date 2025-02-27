"""
Wrapper for aiobotocore BillingandCostManagementPricingCalculator service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bcm_pricing_calculator/)

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
    # Returns type annotated aiobotocore BillingandCostManagementPricingCalculator client
    async with session.bcm_pricing_calculator.create_client() as bcm_pricing_calculator_client:
        bcm_pricing_calculator_client: types_aiobotocore_bcm_pricing_calculator.client.BillingandCostManagementPricingCalculatorClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_bcm_pricing_calculator.client import (
    BillingandCostManagementPricingCalculatorClient,
)

from boto34.aiobotocore.service_factory import ServiceFactory


class BillingandCostManagementPricingCalculatorService(
    ServiceFactory[BillingandCostManagementPricingCalculatorClient]
):
    SERVICE_NAME = "bcm-pricing-calculator"
    _SERVICE_PROP = "bcm_pricing_calculator"
