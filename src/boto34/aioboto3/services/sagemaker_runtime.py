"""
Wrapper for aioboto3 SageMakerRuntime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_runtime/)

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
    # Returns type annotated aioboto3 SageMakerRuntime client
    sagemaker_runtime_client = session.sagemaker_runtime.client()
    sagemaker_runtime_client: types_aiobotocore_sagemaker_runtime.client.SageMakerRuntimeClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_sagemaker_runtime.client import SageMakerRuntimeClient
except ImportError:
    SageMakerRuntimeClient = object  # type: ignore[misc,assignment]


class SageMakerRuntimeService(
    ServiceFactory[SageMakerRuntimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker-runtime"
    _SERVICE_PROP = "sagemaker_runtime"
