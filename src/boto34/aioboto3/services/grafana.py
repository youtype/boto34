"""
Wrapper for aioboto3 ManagedGrafana service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_grafana/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_grafana.client import ManagedGrafanaClient

from boto34.aioboto3.service_factory import ServiceFactory


class ManagedGrafanaService(ServiceFactory[ManagedGrafanaClient]):
    """
    ManagedGrafana service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_grafana/)
    """
