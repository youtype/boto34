"""
Wrapper for boto3 DataAutomationforBedrock service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_bedrock_data_automation.client import DataAutomationforBedrockClient

from boto34.boto3.service_factory import ServiceFactory


class DataAutomationforBedrockService(ServiceFactory[DataAutomationforBedrockClient]):
    """
    DataAutomationforBedrock service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation/)
    """
