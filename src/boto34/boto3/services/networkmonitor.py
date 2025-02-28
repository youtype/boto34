"""
Wrapper for boto3 CloudWatchNetworkMonitor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_networkmonitor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_networkmonitor.client import CloudWatchNetworkMonitorClient

from boto34.boto3.service_factory import ServiceFactory


class CloudWatchNetworkMonitorService(ServiceFactory[CloudWatchNetworkMonitorClient]):
    """
    CloudWatchNetworkMonitor service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_networkmonitor/)
    """
