"""
Wrapper for aiobotocore DataAutomationforBedrock service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_data_automation/)

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
    # Returns type annotated aiobotocore DataAutomationforBedrock client
    async with session.bedrock_data_automation.create_client() as bedrock_data_automation_client:
        bedrock_data_automation_client: (
            types_aiobotocore_bedrock_data_automation.client.DataAutomationforBedrockClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_bedrock_data_automation.client import DataAutomationforBedrockClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_bedrock_data_automation.client import DataAutomationforBedrockClient
except ImportError:
    DataAutomationforBedrockClient = object  # type: ignore[misc,assignment]


class DataAutomationforBedrockService(
    ServiceFactory[DataAutomationforBedrockClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-data-automation"
    _SERVICE_PROP = "bedrock_data_automation"
