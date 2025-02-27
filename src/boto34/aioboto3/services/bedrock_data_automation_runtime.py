"""
Wrapper for aioboto3 RuntimeforBedrockDataAutomation service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock_data_automation_runtime/)

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
    # Returns type annotated aioboto3 RuntimeforBedrockDataAutomation client
    bedrock_data_automation_runtime_client = session.bedrock_data_automation_runtime.client()
    bedrock_data_automation_runtime_client: (
        types_aiobotocore_bedrock_data_automation_runtime.client.RuntimeforBedrockDataAutomationClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_bedrock_data_automation_runtime.client import (
    RuntimeforBedrockDataAutomationClient,
)

from boto34.aioboto3.service_factory import ServiceFactory


class RuntimeforBedrockDataAutomationService(ServiceFactory[RuntimeforBedrockDataAutomationClient]):
    SERVICE_NAME = "bedrock-data-automation-runtime"
    _SERVICE_PROP = "bedrock_data_automation_runtime"
