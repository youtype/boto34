"""
Wrapper for boto3 CloudWatchInternetMonitor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_internetmonitor/)

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
    # Returns type annotated boto3 CloudWatchInternetMonitor client
    internetmonitor_client = session.internetmonitor.client()
    internetmonitor_client: types_boto3_internetmonitor.client.CloudWatchInternetMonitorClient
    ```
"""

from __future__ import annotations

from types_boto3_internetmonitor.client import CloudWatchInternetMonitorClient

from boto34.boto3.service_factory import ServiceFactory


class CloudWatchInternetMonitorService(ServiceFactory[CloudWatchInternetMonitorClient]):
    SERVICE_NAME = "internetmonitor"
    _SERVICE_PROP = "internetmonitor"
