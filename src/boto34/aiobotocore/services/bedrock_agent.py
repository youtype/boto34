"""
Wrapper for aiobotocore AgentsforBedrock service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_bedrock_agent.client import AgentsforBedrockClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AgentsforBedrockService(ServiceFactory[AgentsforBedrockClient]):
    """
    AgentsforBedrock service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent/)
    """
