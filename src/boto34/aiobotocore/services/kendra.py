"""
Wrapper for aiobotocore Kendra service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kendra.client import KendraClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KendraService(ServiceFactory[KendraClient]):
    """
    Kendra service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kendra/)
    """
