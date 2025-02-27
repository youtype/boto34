"""
Wrapper for boto3 NetworkFlowMonitor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_networkflowmonitor/)

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
    # Returns type annotated boto3 NetworkFlowMonitor client
    networkflowmonitor_client = session.networkflowmonitor.client()
    networkflowmonitor_client: types_boto3_networkflowmonitor.client.NetworkFlowMonitorClient
    ```
"""

from __future__ import annotations

from types_boto3_networkflowmonitor.client import NetworkFlowMonitorClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_networkflowmonitor.client import NetworkFlowMonitorClient
except ImportError:
    NetworkFlowMonitorClient = object  # type: ignore[misc,assignment]


class NetworkFlowMonitorService(
    ServiceFactory[NetworkFlowMonitorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "networkflowmonitor"
    _SERVICE_PROP = "networkflowmonitor"
