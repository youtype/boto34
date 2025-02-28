"""
Wrapper for boto3 SecurityLake service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_securitylake/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_securitylake.client import SecurityLakeClient

from boto34.boto3.service_factory import ServiceFactory


class SecurityLakeService(ServiceFactory[SecurityLakeClient]):
    """
    SecurityLake service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_securitylake/)
    """
