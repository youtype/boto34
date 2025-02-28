"""
Wrapper for aioboto3 FIS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_fis/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_fis.client import FISClient

from boto34.aioboto3.service_factory import ServiceFactory


class FISService(ServiceFactory[FISClient]):
    """
    FIS service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_fis/)
    """
