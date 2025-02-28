"""
Wrapper for aiobotocore Route53RecoveryReadiness service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_readiness/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_route53_recovery_readiness.client import Route53RecoveryReadinessClient

from boto34.aiobotocore.service_factory import ServiceFactory


class Route53RecoveryReadinessService(ServiceFactory[Route53RecoveryReadinessClient]):
    """
    Route53RecoveryReadiness service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_readiness/)
    """
