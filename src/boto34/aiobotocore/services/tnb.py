"""
Wrapper for aiobotocore TelcoNetworkBuilder service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_tnb/)

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
    # Returns type annotated aiobotocore TelcoNetworkBuilder client
    async with session.tnb.create_client() as tnb_client:
        tnb_client: types_aiobotocore_tnb.client.TelcoNetworkBuilderClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_tnb.client import TelcoNetworkBuilderClient
except ImportError:
    TelcoNetworkBuilderClient = object  # type: ignore[misc,assignment]


class TelcoNetworkBuilderService(
    ServiceFactory[TelcoNetworkBuilderClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "tnb"
    _SERVICE_PROP = "tnb"
