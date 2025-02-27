"""
Wrapper for aiobotocore CloudWatchLogs service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_logs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore CloudWatchLogs client
    async with session.logs.create_client() as logs_client:
        logs_client: types_aiobotocore_logs.client.CloudWatchLogsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_logs.client import CloudWatchLogsClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_logs.client import CloudWatchLogsClient
except ImportError:
    CloudWatchLogsClient = object  # type: ignore[misc,assignment]


class CloudWatchLogsService(
    ServiceFactory[CloudWatchLogsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "logs"
    _SERVICE_PROP = "logs"
