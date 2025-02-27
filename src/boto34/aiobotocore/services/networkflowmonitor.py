"""
Wrapper for aiobotocore NetworkFlowMonitor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_networkflowmonitor/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore NetworkFlowMonitor client
    async with session.networkflowmonitor.create_client() as networkflowmonitor_client:
        networkflowmonitor_client: types_aiobotocore_networkflowmonitor.client.NetworkFlowMonitorClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_networkflowmonitor.client import NetworkFlowMonitorClient

from boto34.aiobotocore.service_factory import ServiceFactory


class NetworkFlowMonitorService(ServiceFactory[NetworkFlowMonitorClient]):
    SERVICE_NAME = "networkflowmonitor"
    _SERVICE_PROP = "networkflowmonitor"
