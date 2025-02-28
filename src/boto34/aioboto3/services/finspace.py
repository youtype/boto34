"""
Wrapper for aioboto3 Finspace service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_finspace/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_finspace.client import FinspaceClient

from boto34.aioboto3.service_factory import ServiceFactory


class FinspaceService(ServiceFactory[FinspaceClient]):
    """
    Finspace service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_finspace/)
    """
