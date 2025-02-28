"""
Wrapper for aiobotocore TimestreamQuery service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_query/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_timestream_query.client import TimestreamQueryClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TimestreamQueryService(ServiceFactory[TimestreamQueryClient]):
    """
    TimestreamQuery service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_query/)
    """
