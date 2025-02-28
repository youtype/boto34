"""
Wrapper for boto3 ECR service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ecr/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ecr.client import ECRClient

from boto34.boto3.service_factory import ServiceFactory


class ECRService(ServiceFactory[ECRClient]):
    """
    ECR service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ecr/)
    """
