"""
Wrapper for aioboto3 Kendra service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kendra/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kendra.client import KendraClient

from boto34.aioboto3.service_factory import ServiceFactory


class KendraService(ServiceFactory[KendraClient]):
    """
    Kendra service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kendra/)
    """
