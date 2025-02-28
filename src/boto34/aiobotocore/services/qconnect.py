"""
Wrapper for aiobotocore QConnect service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_qconnect.client import QConnectClient

from boto34.aiobotocore.service_factory import ServiceFactory


class QConnectService(ServiceFactory[QConnectClient]):
    """
    QConnect service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_qconnect/)
    """
