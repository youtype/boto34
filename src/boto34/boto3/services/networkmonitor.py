"""
Wrapper for boto3 CloudWatchNetworkMonitor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_networkmonitor/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 CloudWatchNetworkMonitor client
    networkmonitor_client = session.networkmonitor.client()
    networkmonitor_client: types_boto3_networkmonitor.client.CloudWatchNetworkMonitorClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_networkmonitor.client import CloudWatchNetworkMonitorClient
except ImportError:
    CloudWatchNetworkMonitorClient = object  # type: ignore[misc,assignment]


class CloudWatchNetworkMonitorService(
    ServiceFactory[CloudWatchNetworkMonitorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "networkmonitor"
    _SERVICE_PROP = "networkmonitor"
