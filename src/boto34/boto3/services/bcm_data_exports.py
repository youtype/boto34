"""
Wrapper for boto3 BillingandCostManagementDataExports service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bcm_data_exports/)

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
    # Returns type annotated boto3 BillingandCostManagementDataExports client
    bcm_data_exports_client = session.bcm_data_exports.client()
    bcm_data_exports_client: (
        types_boto3_bcm_data_exports.client.BillingandCostManagementDataExportsClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_bcm_data_exports.client import BillingandCostManagementDataExportsClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_bcm_data_exports.client import BillingandCostManagementDataExportsClient
except ImportError:
    BillingandCostManagementDataExportsClient = object  # type: ignore[misc,assignment]


class BillingandCostManagementDataExportsService(
    ServiceFactory[BillingandCostManagementDataExportsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bcm-data-exports"
    _SERVICE_PROP = "bcm_data_exports"
