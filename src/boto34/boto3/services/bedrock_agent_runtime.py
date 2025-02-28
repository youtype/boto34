"""
Wrapper for boto3 AgentsforBedrockRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient

from boto34.boto3.service_factory import ServiceFactory


class AgentsforBedrockRuntimeService(ServiceFactory[AgentsforBedrockRuntimeClient]):
    """
    AgentsforBedrockRuntime service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent_runtime/)
    """
