"""
Wrapper for aioboto3 ConnectCases service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connectcases/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_connectcases.client import ConnectCasesClient

from boto34.aioboto3.service_factory import ServiceFactory


class ConnectCasesService(ServiceFactory[ConnectCasesClient]):
    """
    ConnectCases service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connectcases/)
    """
