"""
Wrapper for aioboto3 NetworkFlowMonitor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_networkflowmonitor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_networkflowmonitor.client import NetworkFlowMonitorClient

from boto34.aioboto3.service_factory import ServiceFactory


class NetworkFlowMonitorService(ServiceFactory[NetworkFlowMonitorClient]):
    """
    NetworkFlowMonitor service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_networkflowmonitor/)
    """
