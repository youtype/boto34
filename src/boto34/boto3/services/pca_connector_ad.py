"""
Wrapper for boto3 PcaConnectorAd service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_pca_connector_ad/)

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
    # Returns type annotated boto3 PcaConnectorAd client
    pca_connector_ad_client = session.pca_connector_ad.client()
    pca_connector_ad_client: types_boto3_pca_connector_ad.client.PcaConnectorAdClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_pca_connector_ad.client import PcaConnectorAdClient
except ImportError:
    PcaConnectorAdClient = object  # type: ignore[misc,assignment]


class PcaConnectorAdService(
    ServiceFactory[PcaConnectorAdClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pca-connector-ad"
    _SERVICE_PROP = "pca_connector_ad"
