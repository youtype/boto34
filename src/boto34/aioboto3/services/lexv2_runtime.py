"""
Wrapper for aioboto3 LexRuntimeV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lexv2_runtime/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lexv2_runtime.client import LexRuntimeV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class LexRuntimeV2Service(ServiceFactory[LexRuntimeV2Client]):
    """
    LexRuntimeV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_lexv2_runtime/)
    """
