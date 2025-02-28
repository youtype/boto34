"""
Wrapper for boto3 Bedrock service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_bedrock.client import BedrockClient

from boto34.boto3.service_factory import ServiceFactory


class BedrockService(ServiceFactory[BedrockClient]):
    """
    Bedrock service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock/)
    """
