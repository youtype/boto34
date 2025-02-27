"""
Wrapper for aiobotocore ApplicationDiscoveryService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_discovery/)

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
    # Returns type annotated aiobotocore ApplicationDiscoveryService client
    async with session.discovery.create_client() as discovery_client:
        discovery_client: types_aiobotocore_discovery.client.ApplicationDiscoveryServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_discovery.client import ApplicationDiscoveryServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_discovery.client import ApplicationDiscoveryServiceClient
except ImportError:
    ApplicationDiscoveryServiceClient = object  # type: ignore[misc,assignment]


class ApplicationDiscoveryServiceService(
    ServiceFactory[ApplicationDiscoveryServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "discovery"
    _SERVICE_PROP = "discovery"
