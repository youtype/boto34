"""
Wrapper for boto3 ServiceDiscovery service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_servicediscovery/)

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
    # Returns type annotated boto3 ServiceDiscovery client
    servicediscovery_client = session.servicediscovery.client()
    servicediscovery_client: types_boto3_servicediscovery.client.ServiceDiscoveryClient
    ```
"""

from __future__ import annotations

from types_boto3_servicediscovery.client import ServiceDiscoveryClient

from boto34.boto3.service_factory import ServiceFactory


class ServiceDiscoveryService(ServiceFactory[ServiceDiscoveryClient]):
    SERVICE_NAME = "servicediscovery"
    _SERVICE_PROP = "servicediscovery"
