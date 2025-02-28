"""
Wrapper for aioboto3 BillingandCostManagementDataExports service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bcm_data_exports/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_bcm_data_exports.client import BillingandCostManagementDataExportsClient

from boto34.aioboto3.service_factory import ServiceFactory


class BillingandCostManagementDataExportsService(
    ServiceFactory[BillingandCostManagementDataExportsClient]
):
    """
    BillingandCostManagementDataExports service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bcm_data_exports/)
    """
