"""
Wrapper for aioboto3 MarketplaceDeploymentService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplace_deployment/)

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
    # Returns type annotated aioboto3 MarketplaceDeploymentService client
    marketplace_deployment_client = session.marketplace_deployment.client()
    marketplace_deployment_client: (
        types_aiobotocore_marketplace_deployment.client.MarketplaceDeploymentServiceClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_marketplace_deployment.client import MarketplaceDeploymentServiceClient
except ImportError:
    MarketplaceDeploymentServiceClient = object  # type: ignore[misc,assignment]


class MarketplaceDeploymentServiceService(
    ServiceFactory[MarketplaceDeploymentServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "marketplace-deployment"
    _SERVICE_PROP = "marketplace_deployment"
