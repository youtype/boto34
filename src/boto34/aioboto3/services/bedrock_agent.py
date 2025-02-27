"""
Wrapper for aioboto3 AgentsforBedrock service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock_agent/)

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
    # Returns type annotated aioboto3 AgentsforBedrock client
    bedrock_agent_client = session.bedrock_agent.client()
    bedrock_agent_client: types_aiobotocore_bedrock_agent.client.AgentsforBedrockClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_bedrock_agent.client import AgentsforBedrockClient
except ImportError:
    AgentsforBedrockClient = object  # type: ignore[misc,assignment]


class AgentsforBedrockService(
    ServiceFactory[AgentsforBedrockClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-agent"
    _SERVICE_PROP = "bedrock_agent"
