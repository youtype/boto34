"""
Wrapper for boto3 SageMaker service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sagemaker.client import SageMakerClient

from boto34.boto3.service_factory import ServiceFactory


class SageMakerService(ServiceFactory[SageMakerClient]):
    """
    SageMaker service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker/)
    """
