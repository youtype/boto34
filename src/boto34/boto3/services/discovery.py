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

from types_boto3_discovery.client import ApplicationDiscoveryServiceClient

from boto34.boto3.service_factory import ServiceFactory


class ApplicationDiscoveryServiceService(ServiceFactory[ApplicationDiscoveryServiceClient]):
    SERVICE_NAME = "discovery"
    _SERVICE_PROP = "discovery"
