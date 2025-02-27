"""
Wrapper for aiobotocore BedrockRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_runtime/)

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
    # Returns type annotated aiobotocore BedrockRuntime client
    async with session.bedrock_runtime.create_client() as bedrock_runtime_client:
        bedrock_runtime_client: types_aiobotocore_bedrock_runtime.client.BedrockRuntimeClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_bedrock_runtime.client import BedrockRuntimeClient
except ImportError:
    BedrockRuntimeClient = object  # type: ignore[misc,assignment]


class BedrockRuntimeService(
    ServiceFactory[BedrockRuntimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-runtime"
    _SERVICE_PROP = "bedrock_runtime"
