"""
Wrapper for aiobotocore FIS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fis/)

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
    # Returns type annotated aiobotocore FIS client
    async with session.fis.create_client() as fis_client:
        fis_client: types_aiobotocore_fis.client.FISClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_fis.client import FISClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_fis.client import FISClient
except ImportError:
    FISClient = object  # type: ignore[misc,assignment]


class FISService(
    ServiceFactory[FISClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "fis"
    _SERVICE_PROP = "fis"
