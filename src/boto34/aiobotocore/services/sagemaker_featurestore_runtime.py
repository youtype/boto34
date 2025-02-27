"""
Wrapper for aiobotocore SageMakerFeatureStoreRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_featurestore_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore SageMakerFeatureStoreRuntime client
    async with (
        session.sagemaker_featurestore_runtime.create_client()
    ) as sagemaker_featurestore_runtime_client:
        sagemaker_featurestore_runtime_client: (
            types_aiobotocore_sagemaker_featurestore_runtime.client.SageMakerFeatureStoreRuntimeClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_featurestore_runtime.client import (
    SageMakerFeatureStoreRuntimeClient,
)

from boto34.aiobotocore.service_factory import ServiceFactory


class SageMakerFeatureStoreRuntimeService(ServiceFactory[SageMakerFeatureStoreRuntimeClient]):
    SERVICE_NAME = "sagemaker-featurestore-runtime"
    _SERVICE_PROP = "sagemaker_featurestore_runtime"
