"""
Wrapper for aiobotocore BedrockRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_bedrock_runtime.client import BedrockRuntimeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class BedrockRuntimeService(ServiceFactory[BedrockRuntimeClient]):
    """
    BedrockRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_runtime/)
    """
