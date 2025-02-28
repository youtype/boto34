"""
Wrapper for boto3 ServiceDiscovery service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_servicediscovery/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_servicediscovery.client import ServiceDiscoveryClient

from boto34.boto3.service_factory import ServiceFactory


class ServiceDiscoveryService(ServiceFactory[ServiceDiscoveryClient]):
    """
    ServiceDiscovery service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_servicediscovery/)
    """
