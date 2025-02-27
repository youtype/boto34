"""
Wrapper for boto3 Bedrock service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock/)

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
    # Returns type annotated boto3 Bedrock client
    bedrock_client = session.bedrock.client()
    bedrock_client: types_boto3_bedrock.client.BedrockClient
    ```
"""

from __future__ import annotations

from types_boto3_bedrock.client import BedrockClient

from boto34.boto3.service_factory import ServiceFactory


class BedrockService(ServiceFactory[BedrockClient]):
    SERVICE_NAME = "bedrock"
    _SERVICE_PROP = "bedrock"
