"""
Wrapper for aiobotocore RePostPrivate service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_repostspace/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_repostspace.client import RePostPrivateClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RePostPrivateService(ServiceFactory[RePostPrivateClient]):
    """
    RePostPrivate service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_repostspace/)
    """
