"""
Wrapper for boto3 ManagedGrafana service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_grafana/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_grafana.client import ManagedGrafanaClient

from boto34.boto3.service_factory import ServiceFactory


class ManagedGrafanaService(ServiceFactory[ManagedGrafanaClient]):
    """
    ManagedGrafana service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_grafana/)
    """
