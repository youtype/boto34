"""
Wrapper for aiobotocore RuntimeforBedrockDataAutomation service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_data_automation_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_bedrock_data_automation_runtime.client import (
    RuntimeforBedrockDataAutomationClient,
)

from boto34.aiobotocore.service_factory import ServiceFactory


class RuntimeforBedrockDataAutomationService(ServiceFactory[RuntimeforBedrockDataAutomationClient]):
    """
    RuntimeforBedrockDataAutomation service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_data_automation_runtime/)
    """
