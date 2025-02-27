"""
Wrapper for aioboto3 BillingandCostManagementDataExports service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bcm_data_exports/)

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
    # Returns type annotated aioboto3 BillingandCostManagementDataExports client
    bcm_data_exports_client = session.bcm_data_exports.client()
    bcm_data_exports_client: (
        types_aiobotocore_bcm_data_exports.client.BillingandCostManagementDataExportsClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_bcm_data_exports.client import BillingandCostManagementDataExportsClient

from boto34.aioboto3.service_factory import ServiceFactory


class BillingandCostManagementDataExportsService(
    ServiceFactory[BillingandCostManagementDataExportsClient]
):
    SERVICE_NAME = "bcm-data-exports"
    _SERVICE_PROP = "bcm_data_exports"
