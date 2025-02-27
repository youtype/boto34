"""
Wrapper for aiobotocore SageMakerRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_runtime/)

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
    # Returns type annotated aiobotocore SageMakerRuntime client
    async with session.sagemaker_runtime.create_client() as sagemaker_runtime_client:
        sagemaker_runtime_client: types_aiobotocore_sagemaker_runtime.client.SageMakerRuntimeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_runtime.client import SageMakerRuntimeClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_sagemaker_runtime.client import SageMakerRuntimeClient
except ImportError:
    SageMakerRuntimeClient = object  # type: ignore[misc,assignment]


class SageMakerRuntimeService(
    ServiceFactory[SageMakerRuntimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker-runtime"
    _SERVICE_PROP = "sagemaker_runtime"
