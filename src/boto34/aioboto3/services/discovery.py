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

from types_aiobotocore_discovery.client import ApplicationDiscoveryServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ApplicationDiscoveryServiceService(ServiceFactory[ApplicationDiscoveryServiceClient]):
    SERVICE_NAME = "discovery"
    _SERVICE_PROP = "discovery"
