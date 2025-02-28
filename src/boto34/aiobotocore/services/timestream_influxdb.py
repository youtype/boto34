"""
Wrapper for aiobotocore TimestreamInfluxDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_influxdb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_timestream_influxdb.client import TimestreamInfluxDBClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TimestreamInfluxDBService(ServiceFactory[TimestreamInfluxDBClient]):
    """
    TimestreamInfluxDB service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_influxdb/)
    """
