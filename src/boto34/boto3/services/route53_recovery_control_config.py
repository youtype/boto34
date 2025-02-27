"""
Wrapper for boto3 Route53RecoveryControlConfig service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_route53_recovery_control_config/)

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
    # Returns type annotated boto3 Route53RecoveryControlConfig client
    route53_recovery_control_config_client = session.route53_recovery_control_config.client()
    route53_recovery_control_config_client: (
        types_boto3_route53_recovery_control_config.client.Route53RecoveryControlConfigClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_route53_recovery_control_config.client import Route53RecoveryControlConfigClient

from boto34.boto3.service_factory import ServiceFactory


class Route53RecoveryControlConfigService(ServiceFactory[Route53RecoveryControlConfigClient]):
    SERVICE_NAME = "route53-recovery-control-config"
    _SERVICE_PROP = "route53_recovery_control_config"
