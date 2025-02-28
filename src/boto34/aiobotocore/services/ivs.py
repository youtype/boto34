"""
Wrapper for aiobotocore IVS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ivs.client import IVSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IVSService(ServiceFactory[IVSClient]):
    """
    IVS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivs/)
    """
