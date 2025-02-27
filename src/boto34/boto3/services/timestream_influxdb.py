"""
Wrapper for boto3 TimestreamInfluxDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_timestream_influxdb/)

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
    # Returns type annotated boto3 TimestreamInfluxDB client
    timestream_influxdb_client = session.timestream_influxdb.client()
    timestream_influxdb_client: types_boto3_timestream_influxdb.client.TimestreamInfluxDBClient
    ```
"""

from __future__ import annotations

from types_boto3_timestream_influxdb.client import TimestreamInfluxDBClient

from boto34.boto3.service_factory import ServiceFactory


class TimestreamInfluxDBService(ServiceFactory[TimestreamInfluxDBClient]):
    SERVICE_NAME = "timestream-influxdb"
    _SERVICE_PROP = "timestream_influxdb"
