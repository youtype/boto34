"""
Wrapper for boto3 RuntimeforBedrockDataAutomation service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/)

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
    # Returns type annotated boto3 RuntimeforBedrockDataAutomation client
    bedrock_data_automation_runtime_client = session.bedrock_data_automation_runtime.client()
    bedrock_data_automation_runtime_client: (
        types_boto3_bedrock_data_automation_runtime.client.RuntimeforBedrockDataAutomationClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_bedrock_data_automation_runtime.client import (
        RuntimeforBedrockDataAutomationClient,
    )
except ImportError:
    RuntimeforBedrockDataAutomationClient = object  # type: ignore[misc,assignment]


class RuntimeforBedrockDataAutomationService(
    ServiceFactory[RuntimeforBedrockDataAutomationClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-data-automation-runtime"
    _SERVICE_PROP = "bedrock_data_automation_runtime"
