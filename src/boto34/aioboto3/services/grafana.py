"""
Wrapper for aioboto3 ManagedGrafana service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_grafana/)

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
    # Returns type annotated aioboto3 ManagedGrafana client
    grafana_client = session.grafana.client()
    grafana_client: types_aiobotocore_grafana.client.ManagedGrafanaClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_grafana.client import ManagedGrafanaClient

from boto34.aioboto3.service_factory import ServiceFactory


class ManagedGrafanaService(ServiceFactory[ManagedGrafanaClient]):
    SERVICE_NAME = "grafana"
    _SERVICE_PROP = "grafana"
