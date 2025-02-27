"""
Wrapper for aioboto3 DataAutomationforBedrock service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock_data_automation/)

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
    # Returns type annotated aioboto3 DataAutomationforBedrock client
    bedrock_data_automation_client = session.bedrock_data_automation.client()
    bedrock_data_automation_client: (
        types_aiobotocore_bedrock_data_automation.client.DataAutomationforBedrockClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_bedrock_data_automation.client import DataAutomationforBedrockClient
except ImportError:
    DataAutomationforBedrockClient = object  # type: ignore[misc,assignment]


class DataAutomationforBedrockService(
    ServiceFactory[DataAutomationforBedrockClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-data-automation"
    _SERVICE_PROP = "bedrock_data_automation"
