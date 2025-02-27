"""
Wrapper for aiobotocore CodeConnections service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeconnections/)

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
    # Returns type annotated aiobotocore CodeConnections client
    async with session.codeconnections.create_client() as codeconnections_client:
        codeconnections_client: types_aiobotocore_codeconnections.client.CodeConnectionsClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_codeconnections.client import CodeConnectionsClient
except ImportError:
    CodeConnectionsClient = object  # type: ignore[misc,assignment]


class CodeConnectionsService(
    ServiceFactory[CodeConnectionsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codeconnections"
    _SERVICE_PROP = "codeconnections"
