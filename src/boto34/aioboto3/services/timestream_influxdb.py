"""
Wrapper for aioboto3 TimestreamInfluxDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_timestream_influxdb/)

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
    # Returns type annotated aioboto3 TimestreamInfluxDB client
    timestream_influxdb_client = session.timestream_influxdb.client()
    timestream_influxdb_client: types_aiobotocore_timestream_influxdb.client.TimestreamInfluxDBClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_timestream_influxdb.client import TimestreamInfluxDBClient
except ImportError:
    TimestreamInfluxDBClient = object  # type: ignore[misc,assignment]


class TimestreamInfluxDBService(
    ServiceFactory[TimestreamInfluxDBClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "timestream-influxdb"
    _SERVICE_PROP = "timestream_influxdb"
