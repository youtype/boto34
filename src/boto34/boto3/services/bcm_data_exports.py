"""
Wrapper for boto3 BillingandCostManagementDataExports service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bcm_data_exports/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_bcm_data_exports.client import BillingandCostManagementDataExportsClient

from boto34.boto3.service_factory import ServiceFactory


class BillingandCostManagementDataExportsService(
    ServiceFactory[BillingandCostManagementDataExportsClient]
):
    """
    BillingandCostManagementDataExports service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bcm_data_exports/)
    """
