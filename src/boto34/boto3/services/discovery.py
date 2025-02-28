"""
Wrapper for boto3 ApplicationDiscoveryService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_discovery/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_discovery.client import ApplicationDiscoveryServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ApplicationDiscoveryServiceService(ServiceFactory[ApplicationDiscoveryServiceClient]):
    """
    ApplicationDiscoveryService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_discovery/)
    """
