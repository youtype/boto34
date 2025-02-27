"""
Wrapper for aiobotocore DataExchange service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dataexchange/)

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
    # Returns type annotated aiobotocore DataExchange client
    async with session.dataexchange.create_client() as dataexchange_client:
        dataexchange_client: types_aiobotocore_dataexchange.client.DataExchangeClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_dataexchange.client import DataExchangeClient
except ImportError:
    DataExchangeClient = object  # type: ignore[misc,assignment]


class DataExchangeService(
    ServiceFactory[DataExchangeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "dataexchange"
    _SERVICE_PROP = "dataexchange"
