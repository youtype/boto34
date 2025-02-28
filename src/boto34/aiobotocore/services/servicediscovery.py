"""
Wrapper for aiobotocore ServiceDiscovery service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_servicediscovery/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_servicediscovery.client import ServiceDiscoveryClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ServiceDiscoveryService(ServiceFactory[ServiceDiscoveryClient]):
    """
    ServiceDiscovery service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_servicediscovery/)
    """
