"""
Wrapper for aiobotocore RuntimeforBedrockDataAutomation service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_data_automation_runtime/)

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
    # Returns type annotated aiobotocore RuntimeforBedrockDataAutomation client
    async with (
        session.bedrock_data_automation_runtime.create_client()
    ) as bedrock_data_automation_runtime_client:
        bedrock_data_automation_runtime_client: types_aiobotocore_bedrock_data_automation_runtime.client.RuntimeforBedrockDataAutomationClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_bedrock_data_automation_runtime.client import (
    RuntimeforBedrockDataAutomationClient,
)

from boto34.aiobotocore.service_factory import ServiceFactory


class RuntimeforBedrockDataAutomationService(ServiceFactory[RuntimeforBedrockDataAutomationClient]):
    SERVICE_NAME = "bedrock-data-automation-runtime"
    _SERVICE_PROP = "bedrock_data_automation_runtime"
