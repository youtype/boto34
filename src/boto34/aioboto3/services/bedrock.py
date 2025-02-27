"""
Wrapper for aioboto3 Bedrock service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock/)

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
    # Returns type annotated aioboto3 Bedrock client
    bedrock_client = session.bedrock.client()
    bedrock_client: types_aiobotocore_bedrock.client.BedrockClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_bedrock.client import BedrockClient
except ImportError:
    BedrockClient = object  # type: ignore[misc,assignment]


class BedrockService(
    ServiceFactory[BedrockClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock"
    _SERVICE_PROP = "bedrock"
