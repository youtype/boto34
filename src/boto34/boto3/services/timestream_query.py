"""
Wrapper for boto3 TimestreamQuery service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_timestream_query/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_timestream_query.client import TimestreamQueryClient

from boto34.boto3.service_factory import ServiceFactory


class TimestreamQueryService(ServiceFactory[TimestreamQueryClient]):
    """
    TimestreamQuery service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_timestream_query/)
    """
