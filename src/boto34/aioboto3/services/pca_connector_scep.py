"""
Wrapper for aioboto3 PrivateCAConnectorforSCEP service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pca_connector_scep/)

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
    # Returns type annotated aioboto3 PrivateCAConnectorforSCEP client
    pca_connector_scep_client = session.pca_connector_scep.client()
    pca_connector_scep_client: (
        types_aiobotocore_pca_connector_scep.client.PrivateCAConnectorforSCEPClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_pca_connector_scep.client import PrivateCAConnectorforSCEPClient
except ImportError:
    PrivateCAConnectorforSCEPClient = object  # type: ignore[misc,assignment]


class PrivateCAConnectorforSCEPService(
    ServiceFactory[PrivateCAConnectorforSCEPClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pca-connector-scep"
    _SERVICE_PROP = "pca_connector_scep"
