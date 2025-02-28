"""
Wrapper for aioboto3 Mgn service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mgn/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mgn.client import MgnClient

from boto34.aioboto3.service_factory import ServiceFactory


class MgnService(ServiceFactory[MgnClient]):
    """
    Mgn service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mgn/)
    """
