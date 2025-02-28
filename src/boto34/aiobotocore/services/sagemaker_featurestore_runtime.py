"""
Wrapper for aiobotocore SageMakerFeatureStoreRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_featurestore_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_featurestore_runtime.client import (
    SageMakerFeatureStoreRuntimeClient,
)

from boto34.aiobotocore.service_factory import ServiceFactory


class SageMakerFeatureStoreRuntimeService(ServiceFactory[SageMakerFeatureStoreRuntimeClient]):
    """
    SageMakerFeatureStoreRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_featurestore_runtime/)
    """
