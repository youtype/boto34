"""
Wrapper for boto3 AgentsforBedrock service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/)

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
    # Returns type annotated boto3 AgentsforBedrock client
    bedrock_agent_client = session.bedrock_agent.client()
    bedrock_agent_client: types_boto3_bedrock_agent.client.AgentsforBedrockClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_bedrock_agent.client import AgentsforBedrockClient
except ImportError:
    AgentsforBedrockClient = object  # type: ignore[misc,assignment]


class AgentsforBedrockService(
    ServiceFactory[AgentsforBedrockClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-agent"
    _SERVICE_PROP = "bedrock_agent"
