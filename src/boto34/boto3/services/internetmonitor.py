"""
Wrapper for boto3 CloudWatchInternetMonitor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_internetmonitor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_internetmonitor.client import CloudWatchInternetMonitorClient

from boto34.boto3.service_factory import ServiceFactory


class CloudWatchInternetMonitorService(ServiceFactory[CloudWatchInternetMonitorClient]):
    """
    CloudWatchInternetMonitor service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_internetmonitor/)
    """
