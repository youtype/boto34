"""
Wrapper for aioboto3 ServiceDiscovery service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_servicediscovery/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_servicediscovery.client import ServiceDiscoveryClient

from boto34.aioboto3.service_factory import ServiceFactory


class ServiceDiscoveryService(ServiceFactory[ServiceDiscoveryClient]):
    """
    ServiceDiscovery service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_servicediscovery/)
    """
