"""
Wrapper for aiobotocore RecycleBin service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rbin/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_rbin.client import RecycleBinClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RecycleBinService(ServiceFactory[RecycleBinClient]):
    """
    RecycleBin service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rbin/)
    """
