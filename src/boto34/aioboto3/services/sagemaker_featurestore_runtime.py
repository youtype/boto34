"""
Wrapper for aioboto3 SageMakerFeatureStoreRuntime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_featurestore_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 SageMakerFeatureStoreRuntime client
    sagemaker_featurestore_runtime_client = session.sagemaker_featurestore_runtime.client()
    sagemaker_featurestore_runtime_client: (
        types_aiobotocore_sagemaker_featurestore_runtime.client.SageMakerFeatureStoreRuntimeClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_sagemaker_featurestore_runtime.client import (
        SageMakerFeatureStoreRuntimeClient,
    )
except ImportError:
    SageMakerFeatureStoreRuntimeClient = object  # type: ignore[misc,assignment]


class SageMakerFeatureStoreRuntimeService(
    ServiceFactory[SageMakerFeatureStoreRuntimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker-featurestore-runtime"
    _SERVICE_PROP = "sagemaker_featurestore_runtime"
