"""
Wrapper for boto3 DataAutomationforBedrock service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation/)

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
    # Returns type annotated boto3 DataAutomationforBedrock client
    bedrock_data_automation_client = session.bedrock_data_automation.client()
    bedrock_data_automation_client: (
        types_boto3_bedrock_data_automation.client.DataAutomationforBedrockClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_bedrock_data_automation.client import DataAutomationforBedrockClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_bedrock_data_automation.client import DataAutomationforBedrockClient
except ImportError:
    DataAutomationforBedrockClient = object  # type: ignore[misc,assignment]


class DataAutomationforBedrockService(
    ServiceFactory[DataAutomationforBedrockClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "bedrock-data-automation"
    _SERVICE_PROP = "bedrock_data_automation"
