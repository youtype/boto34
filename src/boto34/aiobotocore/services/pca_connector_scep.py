"""
Wrapper for aiobotocore PrivateCAConnectorforSCEP service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pca_connector_scep/)

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
    # Returns type annotated aiobotocore PrivateCAConnectorforSCEP client
    async with session.pca_connector_scep.create_client() as pca_connector_scep_client:
        pca_connector_scep_client: (
            types_aiobotocore_pca_connector_scep.client.PrivateCAConnectorforSCEPClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_pca_connector_scep.client import PrivateCAConnectorforSCEPClient
except ImportError:
    PrivateCAConnectorforSCEPClient = object  # type: ignore[misc,assignment]


class PrivateCAConnectorforSCEPService(
    ServiceFactory[PrivateCAConnectorforSCEPClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pca-connector-scep"
    _SERVICE_PROP = "pca_connector_scep"
