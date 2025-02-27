"""
Wrapper for aiobotocore TimestreamQuery service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_query/)

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
    # Returns type annotated aiobotocore TimestreamQuery client
    async with session.timestream_query.create_client() as timestream_query_client:
        timestream_query_client: types_aiobotocore_timestream_query.client.TimestreamQueryClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_timestream_query.client import TimestreamQueryClient
except ImportError:
    TimestreamQueryClient = object  # type: ignore[misc,assignment]


class TimestreamQueryService(
    ServiceFactory[TimestreamQueryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "timestream-query"
    _SERVICE_PROP = "timestream_query"
