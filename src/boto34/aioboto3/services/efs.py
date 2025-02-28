"""
Wrapper for aioboto3 EFS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_efs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_efs.client import EFSClient

from boto34.aioboto3.service_factory import ServiceFactory


class EFSService(ServiceFactory[EFSClient]):
    """
    EFS service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_efs/)
    """
