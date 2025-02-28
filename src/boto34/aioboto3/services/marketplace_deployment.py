"""
Wrapper for aioboto3 MarketplaceDeploymentService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplace_deployment/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_marketplace_deployment.client import MarketplaceDeploymentServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class MarketplaceDeploymentServiceService(ServiceFactory[MarketplaceDeploymentServiceClient]):
    """
    MarketplaceDeploymentService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplace_deployment/)
    """
