"""
Wrapper for aioboto3 Glacier service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_glacier/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_glacier.client import GlacierClient
from types_aiobotocore_glacier.service_resource import GlacierServiceResource

from boto34.aioboto3.service_factory import ServiceResourceFactory


class GlacierService(ServiceResourceFactory[GlacierClient, GlacierServiceResource]):
    """
    Glacier service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_glacier/)
    """
