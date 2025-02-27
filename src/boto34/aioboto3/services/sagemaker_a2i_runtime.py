"""
Wrapper for aioboto3 AugmentedAIRuntime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sagemaker_a2i_runtime/)

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
    # Returns type annotated aioboto3 AugmentedAIRuntime client
    sagemaker_a2i_runtime_client = session.sagemaker_a2i_runtime.client()
    sagemaker_a2i_runtime_client: (
        types_aiobotocore_sagemaker_a2i_runtime.client.AugmentedAIRuntimeClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient

from boto34.aioboto3.service_factory import ServiceFactory


class AugmentedAIRuntimeService(ServiceFactory[AugmentedAIRuntimeClient]):
    SERVICE_NAME = "sagemaker-a2i-runtime"
    _SERVICE_PROP = "sagemaker_a2i_runtime"
