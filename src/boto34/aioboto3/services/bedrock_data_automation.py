"""
Wrapper for aioboto3 DataAutomationforBedrock service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock_data_automation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_bedrock_data_automation.client import DataAutomationforBedrockClient

from boto34.aioboto3.service_factory import ServiceFactory


class DataAutomationforBedrockService(ServiceFactory[DataAutomationforBedrockClient]):
    """
    DataAutomationforBedrock service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_bedrock_data_automation/)
    """
