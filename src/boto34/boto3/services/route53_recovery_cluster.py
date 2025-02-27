"""
Wrapper for boto3 Route53RecoveryCluster service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53_recovery_cluster/)

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
    # Returns type annotated boto3 Route53RecoveryCluster client
    route53_recovery_cluster_client = session.route53_recovery_cluster.client()
    route53_recovery_cluster_client: (
        types_boto3_route53_recovery_cluster.client.Route53RecoveryClusterClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_route53_recovery_cluster.client import Route53RecoveryClusterClient
except ImportError:
    Route53RecoveryClusterClient = object  # type: ignore[misc,assignment]


class Route53RecoveryClusterService(
    ServiceFactory[Route53RecoveryClusterClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "route53-recovery-cluster"
    _SERVICE_PROP = "route53_recovery_cluster"
