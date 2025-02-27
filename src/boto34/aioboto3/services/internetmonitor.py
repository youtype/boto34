"""
Wrapper for aioboto3 CloudWatchInternetMonitor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_internetmonitor/)

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
    # Returns type annotated aioboto3 CloudWatchInternetMonitor client
    internetmonitor_client = session.internetmonitor.client()
    internetmonitor_client: types_aiobotocore_internetmonitor.client.CloudWatchInternetMonitorClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_internetmonitor.client import CloudWatchInternetMonitorClient
except ImportError:
    CloudWatchInternetMonitorClient = object  # type: ignore[misc,assignment]


class CloudWatchInternetMonitorService(
    ServiceFactory[CloudWatchInternetMonitorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "internetmonitor"
    _SERVICE_PROP = "internetmonitor"
