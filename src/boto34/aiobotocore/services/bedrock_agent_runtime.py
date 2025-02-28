"""
Wrapper for aiobotocore AgentsforBedrockRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AgentsforBedrockRuntimeService(ServiceFactory[AgentsforBedrockRuntimeClient]):
    """
    AgentsforBedrockRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/)
    """
