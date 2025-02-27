"""
Wrapper for aiobotocore Route53RecoveryCluster service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_cluster/)

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
    # Returns type annotated aiobotocore Route53RecoveryCluster client
    async with session.route53_recovery_cluster.create_client() as route53_recovery_cluster_client:
        route53_recovery_cluster_client: (
            types_aiobotocore_route53_recovery_cluster.client.Route53RecoveryClusterClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_route53_recovery_cluster.client import Route53RecoveryClusterClient

from boto34.aiobotocore.service_factory import ServiceFactory


class Route53RecoveryClusterService(ServiceFactory[Route53RecoveryClusterClient]):
    SERVICE_NAME = "route53-recovery-cluster"
    _SERVICE_PROP = "route53_recovery_cluster"
