"""
Wrapper for aiobotocore CodeStarconnections service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_connections/)

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
    # Returns type annotated aiobotocore CodeStarconnections client
    async with session.codestar_connections.create_client() as codestar_connections_client:
        codestar_connections_client: (
            types_aiobotocore_codestar_connections.client.CodeStarconnectionsClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_codestar_connections.client import CodeStarconnectionsClient
except ImportError:
    CodeStarconnectionsClient = object  # type: ignore[misc,assignment]


class CodeStarconnectionsService(
    ServiceFactory[CodeStarconnectionsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codestar-connections"
    _SERVICE_PROP = "codestar_connections"
