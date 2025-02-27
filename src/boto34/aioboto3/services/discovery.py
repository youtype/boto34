"""
Wrapper for aioboto3 ApplicationDiscoveryService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_discovery/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 ApplicationDiscoveryService client
    discovery_client = session.discovery.client()
    discovery_client: types_aiobotocore_discovery.client.ApplicationDiscoveryServiceClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_discovery.client import ApplicationDiscoveryServiceClient
except ImportError:
    ApplicationDiscoveryServiceClient = object  # type: ignore[misc,assignment]


class ApplicationDiscoveryServiceService(
    ServiceFactory[ApplicationDiscoveryServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "discovery"
    _SERVICE_PROP = "discovery"
