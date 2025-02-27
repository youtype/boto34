"""
Wrapper for aioboto3 Health service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_health/)

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
    # Returns type annotated aioboto3 Health client
    health_client = session.health.client()
    health_client: types_aiobotocore_health.client.HealthClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_health.client import HealthClient

from boto34.aioboto3.service_factory import ServiceFactory


class HealthService(ServiceFactory[HealthClient]):
    SERVICE_NAME = "health"
    _SERVICE_PROP = "health"
