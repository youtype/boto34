"""
Wrapper for boto3 Health service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_health/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_health.client import HealthClient

from boto34.boto3.service_factory import ServiceFactory


class HealthService(ServiceFactory[HealthClient]):
    """
    Health service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_health/)
    """
