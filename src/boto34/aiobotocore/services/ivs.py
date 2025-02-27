"""
Wrapper for aiobotocore IVS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs/)

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
    # Returns type annotated aiobotocore IVS client
    async with session.ivs.create_client() as ivs_client:
        ivs_client: types_aiobotocore_ivs.client.IVSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ivs.client import IVSClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ivs.client import IVSClient
except ImportError:
    IVSClient = object  # type: ignore[misc,assignment]


class IVSService(
    ServiceFactory[IVSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ivs"
    _SERVICE_PROP = "ivs"
