"""
Wrapper for boto3 TimestreamInfluxDB service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_timestream_influxdb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_timestream_influxdb.client import TimestreamInfluxDBClient

from boto34.boto3.service_factory import ServiceFactory


class TimestreamInfluxDBService(ServiceFactory[TimestreamInfluxDBClient]):
    """
    TimestreamInfluxDB service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_timestream_influxdb/)
    """
