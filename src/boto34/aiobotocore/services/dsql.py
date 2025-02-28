"""
Wrapper for aiobotocore AuroraDSQL service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dsql/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_dsql.client import AuroraDSQLClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AuroraDSQLService(ServiceFactory[AuroraDSQLClient]):
    """
    AuroraDSQL service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_dsql/)
    """
