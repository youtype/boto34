"""
Wrapper for aioboto3 TimestreamQuery service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_timestream_query/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 TimestreamQuery client
    timestream_query_client = session.timestream_query.client()
    timestream_query_client: types_aiobotocore_timestream_query.client.TimestreamQueryClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_timestream_query.client import TimestreamQueryClient
except ImportError:
    TimestreamQueryClient = object  # type: ignore[misc,assignment]


class TimestreamQueryService(
    ServiceFactory[TimestreamQueryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "timestream-query"
    _SERVICE_PROP = "timestream_query"
