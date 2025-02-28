"""
Wrapper for boto3 SageMakerRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sagemaker_runtime.client import SageMakerRuntimeClient

from boto34.boto3.service_factory import ServiceFactory


class SageMakerRuntimeService(ServiceFactory[SageMakerRuntimeClient]):
    """
    SageMakerRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_runtime/)
    """
