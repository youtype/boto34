"""
Wrapper for aioboto3 TimestreamQuery service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_timestream_query/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_timestream_query.client import TimestreamQueryClient

from boto34.aioboto3.service_factory import ServiceFactory


class TimestreamQueryService(ServiceFactory[TimestreamQueryClient]):
    """
    TimestreamQuery service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_timestream_query/)
    """
