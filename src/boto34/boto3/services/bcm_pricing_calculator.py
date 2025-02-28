"""
Wrapper for boto3 BillingandCostManagementPricingCalculator service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bcm_pricing_calculator/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_bcm_pricing_calculator.client import (
    BillingandCostManagementPricingCalculatorClient,
)

from boto34.boto3.service_factory import ServiceFactory


class BillingandCostManagementPricingCalculatorService(
    ServiceFactory[BillingandCostManagementPricingCalculatorClient]
):
    """
    BillingandCostManagementPricingCalculator service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bcm_pricing_calculator/)
    """
