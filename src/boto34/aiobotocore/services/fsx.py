"""
Wrapper for aiobotocore FSx service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fsx/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_fsx.client import FSxClient

from boto34.aiobotocore.service_factory import ServiceFactory


class FSxService(ServiceFactory[FSxClient]):
    """
    FSx service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_fsx/)
    """
