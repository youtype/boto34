"""
Wrapper for aiobotocore TimestreamWrite service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_write/)

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
    # Returns type annotated aiobotocore TimestreamWrite client
    async with session.timestream_write.create_client() as timestream_write_client:
        timestream_write_client: types_aiobotocore_timestream_write.client.TimestreamWriteClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_timestream_write.client import TimestreamWriteClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TimestreamWriteService(ServiceFactory[TimestreamWriteClient]):
    SERVICE_NAME = "timestream-write"
    _SERVICE_PROP = "timestream_write"
