"""
Wrapper for aioboto3 CloudWatchLogs service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_logs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 CloudWatchLogs client
    logs_client = session.logs.client()
    logs_client: types_aiobotocore_logs.client.CloudWatchLogsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_logs.client import CloudWatchLogsClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudWatchLogsService(ServiceFactory[CloudWatchLogsClient]):
    SERVICE_NAME = "logs"
    _SERVICE_PROP = "logs"
