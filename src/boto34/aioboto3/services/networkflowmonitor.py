"""
Wrapper for aioboto3 NetworkFlowMonitor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_networkflowmonitor/)

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
    # Returns type annotated aioboto3 NetworkFlowMonitor client
    networkflowmonitor_client = session.networkflowmonitor.client()
    networkflowmonitor_client: types_aiobotocore_networkflowmonitor.client.NetworkFlowMonitorClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_networkflowmonitor.client import NetworkFlowMonitorClient
except ImportError:
    NetworkFlowMonitorClient = object  # type: ignore[misc,assignment]


class NetworkFlowMonitorService(
    ServiceFactory[NetworkFlowMonitorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "networkflowmonitor"
    _SERVICE_PROP = "networkflowmonitor"
