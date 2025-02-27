"""
Wrapper for boto3 MarketplaceDeploymentService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_deployment/)

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
    # Returns type annotated boto3 MarketplaceDeploymentService client
    marketplace_deployment_client = session.marketplace_deployment.client()
    marketplace_deployment_client: (
        types_boto3_marketplace_deployment.client.MarketplaceDeploymentServiceClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_marketplace_deployment.client import MarketplaceDeploymentServiceClient

from boto34.boto3.service_factory import ServiceFactory


class MarketplaceDeploymentServiceService(ServiceFactory[MarketplaceDeploymentServiceClient]):
    SERVICE_NAME = "marketplace-deployment"
    _SERVICE_PROP = "marketplace_deployment"
