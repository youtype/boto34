"""
Wrapper for aioboto3 CloudWatchNetworkMonitor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_networkmonitor/)

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
    # Returns type annotated aioboto3 CloudWatchNetworkMonitor client
    networkmonitor_client = session.networkmonitor.client()
    networkmonitor_client: types_aiobotocore_networkmonitor.client.CloudWatchNetworkMonitorClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_networkmonitor.client import CloudWatchNetworkMonitorClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudWatchNetworkMonitorService(ServiceFactory[CloudWatchNetworkMonitorClient]):
    SERVICE_NAME = "networkmonitor"
    _SERVICE_PROP = "networkmonitor"
