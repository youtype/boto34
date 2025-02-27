"""
Wrapper for aiobotocore AgentsforBedrockRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/)

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
    # Returns type annotated aiobotocore AgentsforBedrockRuntime client
    async with session.bedrock_agent_runtime.create_client() as bedrock_agent_runtime_client:
        bedrock_agent_runtime_client: (
            types_aiobotocore_bedrock_agent_runtime.client.AgentsforBedrockRuntimeClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AgentsforBedrockRuntimeService(ServiceFactory[AgentsforBedrockRuntimeClient]):
    SERVICE_NAME = "bedrock-agent-runtime"
    _SERVICE_PROP = "bedrock_agent_runtime"
