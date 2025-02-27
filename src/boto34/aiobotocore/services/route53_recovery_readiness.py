"""
Wrapper for aiobotocore Route53RecoveryReadiness service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_readiness/)

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
    # Returns type annotated aiobotocore Route53RecoveryReadiness client
    async with session.route53_recovery_readiness.create_client() as route53_recovery_readiness_client:
        route53_recovery_readiness_client: (
            types_aiobotocore_route53_recovery_readiness.client.Route53RecoveryReadinessClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_route53_recovery_readiness.client import Route53RecoveryReadinessClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_route53_recovery_readiness.client import Route53RecoveryReadinessClient
except ImportError:
    Route53RecoveryReadinessClient = object  # type: ignore[misc,assignment]


class Route53RecoveryReadinessService(
    ServiceFactory[Route53RecoveryReadinessClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "route53-recovery-readiness"
    _SERVICE_PROP = "route53_recovery_readiness"
