"""
Wrapper for aioboto3 RecycleBin service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rbin/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_rbin.client import RecycleBinClient

from boto34.aioboto3.service_factory import ServiceFactory


class RecycleBinService(ServiceFactory[RecycleBinClient]):
    """
    RecycleBin service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rbin/)
    """
