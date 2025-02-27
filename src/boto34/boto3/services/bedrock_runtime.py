"""
Wrapper for boto3 BedrockRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 BedrockRuntime client
    bedrock_runtime_client = session.bedrock_runtime.client()
    bedrock_runtime_client: types_boto3_bedrock_runtime.client.BedrockRuntimeClient
    ```
"""

from __future__ import annotations

from types_boto3_bedrock_runtime.client import BedrockRuntimeClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_bedrock_runtime.client import BedrockRuntimeClient
except ImportError:
    BedrockRuntimeClient = object  # type: ignore[misc,assignment]


class BedrockRuntimeService(
    ServiceFactory[BedrockRuntimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-runtime"
    _SERVICE_PROP = "bedrock_runtime"
