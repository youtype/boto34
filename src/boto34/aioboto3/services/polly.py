"""
Wrapper for aioboto3 Polly service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_polly/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_polly.client import PollyClient

from boto34.aioboto3.service_factory import ServiceFactory


class PollyService(ServiceFactory[PollyClient]):
    """
    Polly service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_polly/)
    """
