"""
Wrapper for aioboto3 CloudWatchNetworkMonitor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_networkmonitor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_networkmonitor.client import CloudWatchNetworkMonitorClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudWatchNetworkMonitorService(ServiceFactory[CloudWatchNetworkMonitorClient]):
    """
    CloudWatchNetworkMonitor service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_networkmonitor/)
    """
