"""
Wrapper for aiobotocore TimestreamInfluxDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_influxdb/)

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
    # Returns type annotated aiobotocore TimestreamInfluxDB client
    async with session.timestream_influxdb.create_client() as timestream_influxdb_client:
        timestream_influxdb_client: (
            types_aiobotocore_timestream_influxdb.client.TimestreamInfluxDBClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_timestream_influxdb.client import TimestreamInfluxDBClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TimestreamInfluxDBService(ServiceFactory[TimestreamInfluxDBClient]):
    SERVICE_NAME = "timestream-influxdb"
    _SERVICE_PROP = "timestream_influxdb"
