"""
Wrapper for aiobotocore BillingandCostManagementPricingCalculator service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bcm_pricing_calculator/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_bcm_pricing_calculator.client import (
    BillingandCostManagementPricingCalculatorClient,
)

from boto34.aiobotocore.service_factory import ServiceFactory


class BillingandCostManagementPricingCalculatorService(
    ServiceFactory[BillingandCostManagementPricingCalculatorClient]
):
    """
    BillingandCostManagementPricingCalculator service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bcm_pricing_calculator/)
    """
