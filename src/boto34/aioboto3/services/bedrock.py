"""
Wrapper for aioboto3 Bedrock service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_bedrock.client import BedrockClient

from boto34.aioboto3.service_factory import ServiceFactory


class BedrockService(ServiceFactory[BedrockClient]):
    """
    Bedrock service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock/)
    """
