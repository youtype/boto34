"""
Wrapper for boto3 HealthLake service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_healthlake/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_healthlake.client import HealthLakeClient

from boto34.boto3.service_factory import ServiceFactory


class HealthLakeService(ServiceFactory[HealthLakeClient]):
    """
    HealthLake service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_healthlake/)
    """
