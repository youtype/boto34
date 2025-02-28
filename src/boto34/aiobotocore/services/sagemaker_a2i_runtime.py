"""
Wrapper for aiobotocore AugmentedAIRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_a2i_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AugmentedAIRuntimeService(ServiceFactory[AugmentedAIRuntimeClient]):
    """
    AugmentedAIRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_a2i_runtime/)
    """
