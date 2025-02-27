"""
Wrapper for aiobotocore AgentsforBedrock service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore AgentsforBedrock client
    async with session.bedrock_agent.create_client() as bedrock_agent_client:
        bedrock_agent_client: types_aiobotocore_bedrock_agent.client.AgentsforBedrockClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_bedrock_agent.client import AgentsforBedrockClient
except ImportError:
    AgentsforBedrockClient = object  # type: ignore[misc,assignment]


class AgentsforBedrockService(
    ServiceFactory[AgentsforBedrockClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-agent"
    _SERVICE_PROP = "bedrock_agent"
