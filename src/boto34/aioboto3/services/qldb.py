"""
Wrapper for aioboto3 QLDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qldb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_qldb.client import QLDBClient

from boto34.aioboto3.service_factory import ServiceFactory


class QLDBService(ServiceFactory[QLDBClient]):
    """
    QLDB service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qldb/)
    """
