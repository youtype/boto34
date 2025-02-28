"""
Wrapper for aioboto3 Route53RecoveryControlConfig service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_route53_recovery_control_config/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_route53_recovery_control_config.client import (
    Route53RecoveryControlConfigClient,
)

from boto34.aioboto3.service_factory import ServiceFactory


class Route53RecoveryControlConfigService(ServiceFactory[Route53RecoveryControlConfigClient]):
    """
    Route53RecoveryControlConfig service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_route53_recovery_control_config/)
    """
