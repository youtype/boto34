"""
Wrapper for aiobotocore Route53RecoveryControlConfig service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_route53_recovery_control_config/)

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
    # Returns type annotated aiobotocore Route53RecoveryControlConfig client
    async with (
        session.route53_recovery_control_config.create_client()
    ) as route53_recovery_control_config_client:
        route53_recovery_control_config_client: (
            types_aiobotocore_route53_recovery_control_config.client.Route53RecoveryControlConfigClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_route53_recovery_control_config.client import (
        Route53RecoveryControlConfigClient,
    )
except ImportError:
    Route53RecoveryControlConfigClient = object  # type: ignore[misc,assignment]


class Route53RecoveryControlConfigService(
    ServiceFactory[Route53RecoveryControlConfigClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "route53-recovery-control-config"
    _SERVICE_PROP = "route53_recovery_control_config"
