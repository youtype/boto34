"""
Wrapper for boto3 TimestreamWrite service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_timestream_write/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_timestream_write.client import TimestreamWriteClient

from boto34.boto3.service_factory import ServiceFactory


class TimestreamWriteService(ServiceFactory[TimestreamWriteClient]):
    """
    TimestreamWrite service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_timestream_write/)
    """
