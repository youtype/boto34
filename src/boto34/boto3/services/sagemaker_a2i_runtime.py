"""
Wrapper for boto3 AugmentedAIRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_a2i_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient

from boto34.boto3.service_factory import ServiceFactory


class AugmentedAIRuntimeService(ServiceFactory[AugmentedAIRuntimeClient]):
    """
    AugmentedAIRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_a2i_runtime/)
    """
