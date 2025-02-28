"""
Wrapper for aiobotocore CloudWatchLogs service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_logs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_logs.client import CloudWatchLogsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchLogsService(ServiceFactory[CloudWatchLogsClient]):
    """
    CloudWatchLogs service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_logs/)
    """
