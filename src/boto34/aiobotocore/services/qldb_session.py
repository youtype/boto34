"""
Wrapper for aiobotocore QLDBSession service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qldb_session/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_qldb_session.client import QLDBSessionClient

from boto34.aiobotocore.service_factory import ServiceFactory


class QLDBSessionService(ServiceFactory[QLDBSessionClient]):
    """
    QLDBSession service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qldb_session/)
    """
