"""
Wrapper for aiobotocore ConnectWisdomService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_wisdom/)

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
    # Returns type annotated aiobotocore ConnectWisdomService client
    async with session.wisdom.create_client() as wisdom_client:
        wisdom_client: types_aiobotocore_wisdom.client.ConnectWisdomServiceClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_wisdom.client import ConnectWisdomServiceClient
except ImportError:
    ConnectWisdomServiceClient = object  # type: ignore[misc,assignment]


class ConnectWisdomServiceService(
    ServiceFactory[ConnectWisdomServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "wisdom"
    _SERVICE_PROP = "wisdom"
