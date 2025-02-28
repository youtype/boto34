"""
Wrapper for aioboto3 FSx service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_fsx/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_fsx.client import FSxClient

from boto34.aioboto3.service_factory import ServiceFactory


class FSxService(ServiceFactory[FSxClient]):
    """
    FSx service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_fsx/)
    """
