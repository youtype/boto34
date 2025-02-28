"""
Wrapper for aioboto3 Comprehend service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_comprehend/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_comprehend.client import ComprehendClient

from boto34.aioboto3.service_factory import ServiceFactory


class ComprehendService(ServiceFactory[ComprehendClient]):
    """
    Comprehend service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_comprehend/)
    """
