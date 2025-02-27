"""
Wrapper for aiobotocore CloudWatchNetworkMonitor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkmonitor/)

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
    # Returns type annotated aiobotocore CloudWatchNetworkMonitor client
    async with session.networkmonitor.create_client() as networkmonitor_client:
        networkmonitor_client: types_aiobotocore_networkmonitor.client.CloudWatchNetworkMonitorClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_networkmonitor.client import CloudWatchNetworkMonitorClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_networkmonitor.client import CloudWatchNetworkMonitorClient
except ImportError:
    CloudWatchNetworkMonitorClient = object  # type: ignore[misc,assignment]


class CloudWatchNetworkMonitorService(
    ServiceFactory[CloudWatchNetworkMonitorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "networkmonitor"
    _SERVICE_PROP = "networkmonitor"
