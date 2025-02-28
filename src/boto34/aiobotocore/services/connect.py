"""
Wrapper for aiobotocore Connect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_connect.client import ConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ConnectService(ServiceFactory[ConnectClient]):
    """
    Connect service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/)
    """
