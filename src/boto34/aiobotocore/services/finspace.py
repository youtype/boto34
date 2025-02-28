"""
Wrapper for aiobotocore Finspace service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_finspace.client import FinspaceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class FinspaceService(ServiceFactory[FinspaceClient]):
    """
    Finspace service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_finspace/)
    """
