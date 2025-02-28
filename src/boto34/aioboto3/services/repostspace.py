"""
Wrapper for aioboto3 RePostPrivate service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_repostspace/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_repostspace.client import RePostPrivateClient

from boto34.aioboto3.service_factory import ServiceFactory


class RePostPrivateService(ServiceFactory[RePostPrivateClient]):
    """
    RePostPrivate service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_repostspace/)
    """
