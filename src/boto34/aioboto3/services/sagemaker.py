"""
Wrapper for aioboto3 SageMaker service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sagemaker.client import SageMakerClient

from boto34.aioboto3.service_factory import ServiceFactory


class SageMakerService(ServiceFactory[SageMakerClient]):
    """
    SageMaker service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker/)
    """
