"""
Wrapper for boto3 SSM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ssm.client import SSMClient

from boto34.boto3.service_factory import ServiceFactory


class SSMService(ServiceFactory[SSMClient]):
    """
    SSM service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm/)
    """
