"""
Wrapper for aioboto3 IVS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ivs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ivs.client import IVSClient

from boto34.aioboto3.service_factory import ServiceFactory


class IVSService(ServiceFactory[IVSClient]):
    """
    IVS service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ivs/)
    """
