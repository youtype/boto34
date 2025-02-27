"""
Wrapper for boto3 AgentsforBedrockRuntime service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_agent_runtime/)

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
    # Returns type annotated boto3 AgentsforBedrockRuntime client
    bedrock_agent_runtime_client = session.bedrock_agent_runtime.client()
    bedrock_agent_runtime_client: types_boto3_bedrock_agent_runtime.client.AgentsforBedrockRuntimeClient
    ```
"""

from __future__ import annotations

from types_boto3_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient

from boto34.boto3.service_factory import ServiceFactory


class AgentsforBedrockRuntimeService(ServiceFactory[AgentsforBedrockRuntimeClient]):
    SERVICE_NAME = "bedrock-agent-runtime"
    _SERVICE_PROP = "bedrock_agent_runtime"
