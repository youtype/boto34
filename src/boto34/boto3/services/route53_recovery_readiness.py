"""
Wrapper for boto3 Route53RecoveryReadiness service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53_recovery_readiness/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_route53_recovery_readiness.client import Route53RecoveryReadinessClient

from boto34.boto3.service_factory import ServiceFactory


class Route53RecoveryReadinessService(ServiceFactory[Route53RecoveryReadinessClient]):
    """
    Route53RecoveryReadiness service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53_recovery_readiness/)
    """
