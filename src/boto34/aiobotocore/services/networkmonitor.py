"""
Wrapper for aiobotocore CloudWatchNetworkMonitor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkmonitor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_networkmonitor.client import CloudWatchNetworkMonitorClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchNetworkMonitorService(ServiceFactory[CloudWatchNetworkMonitorClient]):
    """
    CloudWatchNetworkMonitor service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkmonitor/)
    """
