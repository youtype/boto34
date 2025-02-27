"""
Wrapper for aiobotocore FSx service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fsx/)

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
    # Returns type annotated aiobotocore FSx client
    async with session.fsx.create_client() as fsx_client:
        fsx_client: types_aiobotocore_fsx.client.FSxClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_fsx.client import FSxClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_fsx.client import FSxClient
except ImportError:
    FSxClient = object  # type: ignore[misc,assignment]


class FSxService(
    ServiceFactory[FSxClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "fsx"
    _SERVICE_PROP = "fsx"
