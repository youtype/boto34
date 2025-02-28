"""
Wrapper for aioboto3 SageMakerRuntime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_runtime.client import SageMakerRuntimeClient

from boto34.aioboto3.service_factory import ServiceFactory


class SageMakerRuntimeService(ServiceFactory[SageMakerRuntimeClient]):
    """
    SageMakerRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_runtime/)
    """
