"""
Wrapper for boto3 MarketplaceDeploymentService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_deployment/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_marketplace_deployment.client import MarketplaceDeploymentServiceClient

from boto34.boto3.service_factory import ServiceFactory


class MarketplaceDeploymentServiceService(ServiceFactory[MarketplaceDeploymentServiceClient]):
    """
    MarketplaceDeploymentService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_deployment/)
    """
