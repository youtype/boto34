"""
Wrapper for aioboto3 ServiceDiscovery service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_servicediscovery/)

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
    # Returns type annotated aioboto3 ServiceDiscovery client
    servicediscovery_client = session.servicediscovery.client()
    servicediscovery_client: types_aiobotocore_servicediscovery.client.ServiceDiscoveryClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_servicediscovery.client import ServiceDiscoveryClient
except ImportError:
    ServiceDiscoveryClient = object  # type: ignore[misc,assignment]


class ServiceDiscoveryService(
    ServiceFactory[ServiceDiscoveryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "servicediscovery"
    _SERVICE_PROP = "servicediscovery"
