"""
Wrapper for boto3 TimestreamQuery service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_timestream_query/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 TimestreamQuery client
    timestream_query_client = session.timestream_query.client()
    timestream_query_client: types_boto3_timestream_query.client.TimestreamQueryClient
    ```
"""

from __future__ import annotations

from types_boto3_timestream_query.client import TimestreamQueryClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_timestream_query.client import TimestreamQueryClient
except ImportError:
    TimestreamQueryClient = object  # type: ignore[misc,assignment]


class TimestreamQueryService(
    ServiceFactory[TimestreamQueryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "timestream-query"
    _SERVICE_PROP = "timestream_query"
