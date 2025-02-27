"""
Wrapper for boto3 ApplicationDiscoveryService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_discovery/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ApplicationDiscoveryService client
    discovery_client = session.discovery.client()
    discovery_client: types_boto3_discovery.client.ApplicationDiscoveryServiceClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_discovery.client import ApplicationDiscoveryServiceClient
except ImportError:
    ApplicationDiscoveryServiceClient = object  # type: ignore[misc,assignment]


class ApplicationDiscoveryServiceService(
    ServiceFactory[ApplicationDiscoveryServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "discovery"
    _SERVICE_PROP = "discovery"
