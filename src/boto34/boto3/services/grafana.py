"""
Wrapper for boto3 ManagedGrafana service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_grafana/)

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
    # Returns type annotated boto3 ManagedGrafana client
    grafana_client = session.grafana.client()
    grafana_client: types_boto3_grafana.client.ManagedGrafanaClient
    ```
"""

from __future__ import annotations

from types_boto3_grafana.client import ManagedGrafanaClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_grafana.client import ManagedGrafanaClient
except ImportError:
    ManagedGrafanaClient = object  # type: ignore[misc,assignment]


class ManagedGrafanaService(
    ServiceFactory[ManagedGrafanaClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "grafana"
    _SERVICE_PROP = "grafana"
