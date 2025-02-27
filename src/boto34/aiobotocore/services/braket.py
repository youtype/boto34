"""
Wrapper for aiobotocore Braket service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_braket/)

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
    # Returns type annotated aiobotocore Braket client
    async with session.braket.create_client() as braket_client:
        braket_client: types_aiobotocore_braket.client.BraketClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_braket.client import BraketClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_braket.client import BraketClient
except ImportError:
    BraketClient = object  # type: ignore[misc,assignment]


class BraketService(
    ServiceFactory[BraketClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "braket"
    _SERVICE_PROP = "braket"
