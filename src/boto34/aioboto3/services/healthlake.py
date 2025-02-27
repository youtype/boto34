"""
Wrapper for aioboto3 HealthLake service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_healthlake/)

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
    # Returns type annotated aioboto3 HealthLake client
    healthlake_client = session.healthlake.client()
    healthlake_client: types_aiobotocore_healthlake.client.HealthLakeClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_healthlake.client import HealthLakeClient
except ImportError:
    HealthLakeClient = object  # type: ignore[misc,assignment]


class HealthLakeService(
    ServiceFactory[HealthLakeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "healthlake"
    _SERVICE_PROP = "healthlake"
