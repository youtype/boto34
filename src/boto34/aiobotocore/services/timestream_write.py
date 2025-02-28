"""
Wrapper for aiobotocore TimestreamWrite service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_write/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_timestream_write.client import TimestreamWriteClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TimestreamWriteService(ServiceFactory[TimestreamWriteClient]):
    """
    TimestreamWrite service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_write/)
    """
