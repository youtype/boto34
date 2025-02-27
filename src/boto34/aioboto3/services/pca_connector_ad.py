"""
Wrapper for aioboto3 PcaConnectorAd service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pca_connector_ad/)

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
    # Returns type annotated aioboto3 PcaConnectorAd client
    pca_connector_ad_client = session.pca_connector_ad.client()
    pca_connector_ad_client: types_aiobotocore_pca_connector_ad.client.PcaConnectorAdClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_pca_connector_ad.client import PcaConnectorAdClient

from boto34.aioboto3.service_factory import ServiceFactory


class PcaConnectorAdService(ServiceFactory[PcaConnectorAdClient]):
    SERVICE_NAME = "pca-connector-ad"
    _SERVICE_PROP = "pca_connector_ad"
