"""
Wrapper for aiobotocore Mgn service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mgn.client import MgnClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MgnService(ServiceFactory[MgnClient]):
    """
    Mgn service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/)
    """
