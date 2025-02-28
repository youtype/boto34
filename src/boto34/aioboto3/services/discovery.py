"""
Wrapper for aioboto3 ApplicationDiscoveryService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_discovery/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_discovery.client import ApplicationDiscoveryServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ApplicationDiscoveryServiceService(ServiceFactory[ApplicationDiscoveryServiceClient]):
    """
    ApplicationDiscoveryService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_discovery/)
    """
