"""
Wrapper for aioboto3 TimestreamInfluxDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_timestream_influxdb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_timestream_influxdb.client import TimestreamInfluxDBClient

from boto34.aioboto3.service_factory import ServiceFactory


class TimestreamInfluxDBService(ServiceFactory[TimestreamInfluxDBClient]):
    """
    TimestreamInfluxDB service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_timestream_influxdb/)
    """
