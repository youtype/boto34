"""
Wrapper for boto3 LexRuntimeV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lexv2_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_lexv2_runtime.client import LexRuntimeV2Client

from boto34.boto3.service_factory import ServiceFactory


class LexRuntimeV2Service(ServiceFactory[LexRuntimeV2Client]):
    """
    LexRuntimeV2 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_lexv2_runtime/)
    """
