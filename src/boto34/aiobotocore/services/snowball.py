"""
Wrapper for aiobotocore Snowball service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_snowball/)

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
    # Returns type annotated aiobotocore Snowball client
    async with session.snowball.create_client() as snowball_client:
        snowball_client: types_aiobotocore_snowball.client.SnowballClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_snowball.client import SnowballClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_snowball.client import SnowballClient
except ImportError:
    SnowballClient = object  # type: ignore[misc,assignment]


class SnowballService(
    ServiceFactory[SnowballClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "snowball"
    _SERVICE_PROP = "snowball"
