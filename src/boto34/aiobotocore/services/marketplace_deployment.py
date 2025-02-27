"""
Wrapper for aiobotocore MarketplaceDeploymentService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_deployment/)

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
    # Returns type annotated aiobotocore MarketplaceDeploymentService client
    async with session.marketplace_deployment.create_client() as marketplace_deployment_client:
        marketplace_deployment_client: (
            types_aiobotocore_marketplace_deployment.client.MarketplaceDeploymentServiceClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_marketplace_deployment.client import MarketplaceDeploymentServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_marketplace_deployment.client import MarketplaceDeploymentServiceClient
except ImportError:
    MarketplaceDeploymentServiceClient = object  # type: ignore[misc,assignment]


class MarketplaceDeploymentServiceService(
    ServiceFactory[MarketplaceDeploymentServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "marketplace-deployment"
    _SERVICE_PROP = "marketplace_deployment"
