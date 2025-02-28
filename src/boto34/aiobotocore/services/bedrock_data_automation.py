"""
Wrapper for aiobotocore DataAutomationforBedrock service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_data_automation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_bedrock_data_automation.client import DataAutomationforBedrockClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DataAutomationforBedrockService(ServiceFactory[DataAutomationforBedrockClient]):
    """
    DataAutomationforBedrock service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_data_automation/)
    """
