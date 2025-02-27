"""
Wrapper for aiobotocore Chime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime/)

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
    # Returns type annotated aiobotocore Chime client
    async with session.chime.create_client() as chime_client:
        chime_client: types_aiobotocore_chime.client.ChimeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_chime.client import ChimeClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_chime.client import ChimeClient
except ImportError:
    ChimeClient = object  # type: ignore[misc,assignment]


class ChimeService(
    ServiceFactory[ChimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime"
    _SERVICE_PROP = "chime"
