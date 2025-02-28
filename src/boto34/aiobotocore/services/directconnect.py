"""
Wrapper for aiobotocore DirectConnect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_directconnect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_directconnect.client import DirectConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DirectConnectService(ServiceFactory[DirectConnectClient]):
    """
    DirectConnect service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_directconnect/)
    """
