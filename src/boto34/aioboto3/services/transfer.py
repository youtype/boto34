"""
Wrapper for aioboto3 Transfer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_transfer/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_transfer.client import TransferClient

from boto34.aioboto3.service_factory import ServiceFactory


class TransferService(ServiceFactory[TransferClient]):
    """
    Transfer service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_transfer/)
    """
