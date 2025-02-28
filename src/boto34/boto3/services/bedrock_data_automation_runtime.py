"""
Wrapper for boto3 RuntimeforBedrockDataAutomation service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_bedrock_data_automation_runtime.client import RuntimeforBedrockDataAutomationClient

from boto34.boto3.service_factory import ServiceFactory


class RuntimeforBedrockDataAutomationService(ServiceFactory[RuntimeforBedrockDataAutomationClient]):
    """
    RuntimeforBedrockDataAutomation service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_bedrock_data_automation_runtime/)
    """
