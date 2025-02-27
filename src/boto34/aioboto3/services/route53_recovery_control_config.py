"""
Wrapper for aioboto3 Route53RecoveryControlConfig service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_route53_recovery_control_config/)

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
    # Returns type annotated aioboto3 Route53RecoveryControlConfig client
    route53_recovery_control_config_client = session.route53_recovery_control_config.client()
    route53_recovery_control_config_client: (
        types_aiobotocore_route53_recovery_control_config.client.Route53RecoveryControlConfigClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_route53_recovery_control_config.client import (
    Route53RecoveryControlConfigClient,
)

from boto34.aioboto3.service_factory import ServiceFactory


class Route53RecoveryControlConfigService(ServiceFactory[Route53RecoveryControlConfigClient]):
    SERVICE_NAME = "route53-recovery-control-config"
    _SERVICE_PROP = "route53_recovery_control_config"
