"""
Wrapper for aiobotocore HealthLake service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_healthlake/)

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
    # Returns type annotated aiobotocore HealthLake client
    async with session.healthlake.create_client() as healthlake_client:
        healthlake_client: types_aiobotocore_healthlake.client.HealthLakeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_healthlake.client import HealthLakeClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_healthlake.client import HealthLakeClient
except ImportError:
    HealthLakeClient = object  # type: ignore[misc,assignment]


class HealthLakeService(
    ServiceFactory[HealthLakeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "healthlake"
    _SERVICE_PROP = "healthlake"
