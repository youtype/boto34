"""
Wrapper for aioboto3 TimestreamWrite service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_timestream_write/)

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
    # Returns type annotated aioboto3 TimestreamWrite client
    timestream_write_client = session.timestream_write.client()
    timestream_write_client: types_aiobotocore_timestream_write.client.TimestreamWriteClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_timestream_write.client import TimestreamWriteClient

from boto34.aioboto3.service_factory import ServiceFactory


class TimestreamWriteService(ServiceFactory[TimestreamWriteClient]):
    SERVICE_NAME = "timestream-write"
    _SERVICE_PROP = "timestream_write"
