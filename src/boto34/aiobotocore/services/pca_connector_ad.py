"""
Wrapper for aiobotocore PcaConnectorAd service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_ad/)

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
    # Returns type annotated aiobotocore PcaConnectorAd client
    async with session.pca_connector_ad.create_client() as pca_connector_ad_client:
        pca_connector_ad_client: types_aiobotocore_pca_connector_ad.client.PcaConnectorAdClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_pca_connector_ad.client import PcaConnectorAdClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_pca_connector_ad.client import PcaConnectorAdClient
except ImportError:
    PcaConnectorAdClient = object  # type: ignore[misc,assignment]


class PcaConnectorAdService(
    ServiceFactory[PcaConnectorAdClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pca-connector-ad"
    _SERVICE_PROP = "pca_connector_ad"
