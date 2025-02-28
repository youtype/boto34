"""
Wrapper for aioboto3 SimpleDB service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sdb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_sdb.client import SimpleDBClient

from boto34.aioboto3.service_factory import ServiceFactory


class SimpleDBService(ServiceFactory[SimpleDBClient]):
    """
    SimpleDB service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_sdb/)
    """
