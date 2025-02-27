"""
Wrapper for aiobotocore Health service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_health/)

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
    # Returns type annotated aiobotocore Health client
    async with session.health.create_client() as health_client:
        health_client: types_aiobotocore_health.client.HealthClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_health.client import HealthClient
except ImportError:
    HealthClient = object  # type: ignore[misc,assignment]


class HealthService(
    ServiceFactory[HealthClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "health"
    _SERVICE_PROP = "health"
