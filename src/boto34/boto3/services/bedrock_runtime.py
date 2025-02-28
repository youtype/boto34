"""
Wrapper for boto3 BedrockRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_bedrock_runtime.client import BedrockRuntimeClient

from boto34.boto3.service_factory import ServiceFactory


class BedrockRuntimeService(ServiceFactory[BedrockRuntimeClient]):
    """
    BedrockRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_runtime/)
    """
