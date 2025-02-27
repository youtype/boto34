"""
Wrapper for aiobotocore SageMaker service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker/)

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
    # Returns type annotated aiobotocore SageMaker client
    async with session.sagemaker.create_client() as sagemaker_client:
        sagemaker_client: types_aiobotocore_sagemaker.client.SageMakerClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_sagemaker.client import SageMakerClient
except ImportError:
    SageMakerClient = object  # type: ignore[misc,assignment]


class SageMakerService(
    ServiceFactory[SageMakerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker"
    _SERVICE_PROP = "sagemaker"
