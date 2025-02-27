"""
Wrapper for aiobotocore CloudWatchInternetMonitor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_internetmonitor/)

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
    # Returns type annotated aiobotocore CloudWatchInternetMonitor client
    async with session.internetmonitor.create_client() as internetmonitor_client:
        internetmonitor_client: types_aiobotocore_internetmonitor.client.CloudWatchInternetMonitorClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_internetmonitor.client import CloudWatchInternetMonitorClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_internetmonitor.client import CloudWatchInternetMonitorClient
except ImportError:
    CloudWatchInternetMonitorClient = object  # type: ignore[misc,assignment]


class CloudWatchInternetMonitorService(
    ServiceFactory[CloudWatchInternetMonitorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "internetmonitor"
    _SERVICE_PROP = "internetmonitor"
