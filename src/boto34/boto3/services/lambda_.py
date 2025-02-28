"""
Wrapper for boto3 Lambda service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lambda/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_lambda.client import LambdaClient

from boto34.boto3.service_factory import ServiceFactory


class LambdaService(ServiceFactory[LambdaClient]):
    """
    Lambda service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lambda/)
    """
