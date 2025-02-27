"""
Wrapper for aioboto3 SageMaker service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker/)

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
    # Returns type annotated aioboto3 SageMaker client
    sagemaker_client = session.sagemaker.client()
    sagemaker_client: types_aiobotocore_sagemaker.client.SageMakerClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_sagemaker.client import SageMakerClient
except ImportError:
    SageMakerClient = object  # type: ignore[misc,assignment]


class SageMakerService(
    ServiceFactory[SageMakerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "sagemaker"
    _SERVICE_PROP = "sagemaker"
