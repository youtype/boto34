"""
Wrapper for boto3 Route53RecoveryReadiness service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53_recovery_readiness/)

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
    # Returns type annotated boto3 Route53RecoveryReadiness client
    route53_recovery_readiness_client = session.route53_recovery_readiness.client()
    route53_recovery_readiness_client: (
        types_boto3_route53_recovery_readiness.client.Route53RecoveryReadinessClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_route53_recovery_readiness.client import Route53RecoveryReadinessClient

from boto34.boto3.service_factory import ServiceFactory


class Route53RecoveryReadinessService(ServiceFactory[Route53RecoveryReadinessClient]):
    SERVICE_NAME = "route53-recovery-readiness"
    _SERVICE_PROP = "route53_recovery_readiness"
