"""
Wrapper for aiobotocore Support service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_support.client import SupportClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SupportService(ServiceFactory[SupportClient]):
    """
    Support service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support/)
    """
