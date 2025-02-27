"""
Wrapper for aioboto3 AgentsforBedrockRuntime service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock_agent_runtime/)

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
    # Returns type annotated aioboto3 AgentsforBedrockRuntime client
    bedrock_agent_runtime_client = session.bedrock_agent_runtime.client()
    bedrock_agent_runtime_client: (
        types_aiobotocore_bedrock_agent_runtime.client.AgentsforBedrockRuntimeClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient
except ImportError:
    AgentsforBedrockRuntimeClient = object  # type: ignore[misc,assignment]


class AgentsforBedrockRuntimeService(
    ServiceFactory[AgentsforBedrockRuntimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-agent-runtime"
    _SERVICE_PROP = "bedrock_agent_runtime"
