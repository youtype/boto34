"""
Wrapper for boto3 TimestreamWrite service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_timestream_write/)

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
    # Returns type annotated boto3 TimestreamWrite client
    timestream_write_client = session.timestream_write.client()
    timestream_write_client: types_boto3_timestream_write.client.TimestreamWriteClient
    ```
"""

from __future__ import annotations

from types_boto3_timestream_write.client import TimestreamWriteClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_timestream_write.client import TimestreamWriteClient
except ImportError:
    TimestreamWriteClient = object  # type: ignore[misc,assignment]


class TimestreamWriteService(
    ServiceFactory[TimestreamWriteClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "timestream-write"
    _SERVICE_PROP = "timestream_write"
