"""
Wrapper for aiobotocore Braket service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_braket/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_braket.client import BraketClient

from boto34.aiobotocore.service_factory import ServiceFactory


class BraketService(ServiceFactory[BraketClient]):
    """
    Braket service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_braket/)
    """
