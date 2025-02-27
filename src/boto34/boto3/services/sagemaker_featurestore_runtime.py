"""
Wrapper for boto3 SageMakerFeatureStoreRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_sagemaker_featurestore_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 SageMakerFeatureStoreRuntime client
    sagemaker_featurestore_runtime_client = session.sagemaker_featurestore_runtime.client()
    sagemaker_featurestore_runtime_client: (
        types_boto3_sagemaker_featurestore_runtime.client.SageMakerFeatureStoreRuntimeClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_sagemaker_featurestore_runtime.client import SageMakerFeatureStoreRuntimeClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_sagemaker_featurestore_runtime.client import SageMakerFeatureStoreRuntimeClient
except ImportError:
    SageMakerFeatureStoreRuntimeClient = object  # type: ignore[misc,assignment]


class SageMakerFeatureStoreRuntimeService(
    ServiceFactory[SageMakerFeatureStoreRuntimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker-featurestore-runtime"
    _SERVICE_PROP = "sagemaker_featurestore_runtime"
