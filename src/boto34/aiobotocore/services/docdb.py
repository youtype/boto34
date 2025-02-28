"""
Wrapper for aiobotocore DocDB service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_docdb/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_docdb.client import DocDBClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DocDBService(ServiceFactory[DocDBClient]):
    """
    DocDB service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_docdb/)
    """
