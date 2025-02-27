"""
Wrapper for aiobotocore BillingandCostManagementDataExports service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bcm_data_exports/)

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
    # Returns type annotated aiobotocore BillingandCostManagementDataExports client
    async with session.bcm_data_exports.create_client() as bcm_data_exports_client:
        bcm_data_exports_client: (
            types_aiobotocore_bcm_data_exports.client.BillingandCostManagementDataExportsClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_bcm_data_exports.client import BillingandCostManagementDataExportsClient
except ImportError:
    BillingandCostManagementDataExportsClient = object  # type: ignore[misc,assignment]


class BillingandCostManagementDataExportsService(
    ServiceFactory[BillingandCostManagementDataExportsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bcm-data-exports"
    _SERVICE_PROP = "bcm_data_exports"
