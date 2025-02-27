"""
Wrapper for aiobotocore AugmentedAIRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_a2i_runtime/)

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
    # Returns type annotated aiobotocore AugmentedAIRuntime client
    async with session.sagemaker_a2i_runtime.create_client() as sagemaker_a2i_runtime_client:
        sagemaker_a2i_runtime_client: (
            types_aiobotocore_sagemaker_a2i_runtime.client.AugmentedAIRuntimeClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AugmentedAIRuntimeService(ServiceFactory[AugmentedAIRuntimeClient]):
    SERVICE_NAME = "sagemaker-a2i-runtime"
    _SERVICE_PROP = "sagemaker_a2i_runtime"
