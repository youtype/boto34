"""
Wrapper for aiobotocore ManagedGrafana service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_grafana/)

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
    # Returns type annotated aiobotocore ManagedGrafana client
    async with session.grafana.create_client() as grafana_client:
        grafana_client: types_aiobotocore_grafana.client.ManagedGrafanaClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_grafana.client import ManagedGrafanaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ManagedGrafanaService(ServiceFactory[ManagedGrafanaClient]):
    SERVICE_NAME = "grafana"
    _SERVICE_PROP = "grafana"
