"""
Wrapper for aioboto3 Route53RecoveryReadiness service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_route53_recovery_readiness/)

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
    # Returns type annotated aioboto3 Route53RecoveryReadiness client
    route53_recovery_readiness_client = session.route53_recovery_readiness.client()
    route53_recovery_readiness_client: (
        types_aiobotocore_route53_recovery_readiness.client.Route53RecoveryReadinessClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_route53_recovery_readiness.client import Route53RecoveryReadinessClient
except ImportError:
    Route53RecoveryReadinessClient = object  # type: ignore[misc,assignment]


class Route53RecoveryReadinessService(
    ServiceFactory[Route53RecoveryReadinessClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "route53-recovery-readiness"
    _SERVICE_PROP = "route53_recovery_readiness"
