"""
Wrapper for boto3 AgentsforBedrock service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_bedrock_agent.client import AgentsforBedrockClient

from boto34.boto3.service_factory import ServiceFactory


class AgentsforBedrockService(ServiceFactory[AgentsforBedrockClient]):
    """
    AgentsforBedrock service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent/)
    """
