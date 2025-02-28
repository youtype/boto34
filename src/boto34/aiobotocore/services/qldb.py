"""
Wrapper for aiobotocore QLDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qldb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_qldb.client import QLDBClient

from boto34.aiobotocore.service_factory import ServiceFactory


class QLDBService(ServiceFactory[QLDBClient]):
    """
    QLDB service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qldb/)
    """
