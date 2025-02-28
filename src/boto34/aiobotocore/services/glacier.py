"""
Wrapper for aiobotocore Glacier service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_glacier.client import GlacierClient

from boto34.aiobotocore.service_factory import ServiceFactory


class GlacierService(ServiceFactory[GlacierClient]):
    """
    Glacier service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_glacier/)
    """
