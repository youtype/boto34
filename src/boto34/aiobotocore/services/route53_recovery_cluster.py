"""
Wrapper for aiobotocore Route53RecoveryCluster service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_cluster/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_route53_recovery_cluster.client import Route53RecoveryClusterClient

from boto34.aiobotocore.service_factory import ServiceFactory


class Route53RecoveryClusterService(ServiceFactory[Route53RecoveryClusterClient]):
    """
    Route53RecoveryCluster service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_cluster/)
    """
