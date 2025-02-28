"""
Wrapper for aiobotocore CloudWatchInternetMonitor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_internetmonitor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_internetmonitor.client import CloudWatchInternetMonitorClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudWatchInternetMonitorService(ServiceFactory[CloudWatchInternetMonitorClient]):
    """
    CloudWatchInternetMonitor service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_internetmonitor/)
    """
