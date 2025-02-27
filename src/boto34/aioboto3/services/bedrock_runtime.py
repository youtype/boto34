"""
Wrapper for aioboto3 BedrockRuntime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock_runtime/)

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
    # Returns type annotated aioboto3 BedrockRuntime client
    bedrock_runtime_client = session.bedrock_runtime.client()
    bedrock_runtime_client: types_aiobotocore_bedrock_runtime.client.BedrockRuntimeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_bedrock_runtime.client import BedrockRuntimeClient

from boto34.aioboto3.service_factory import ServiceFactory


class BedrockRuntimeService(ServiceFactory[BedrockRuntimeClient]):
    SERVICE_NAME = "bedrock-runtime"
    _SERVICE_PROP = "bedrock_runtime"
