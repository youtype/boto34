"""
Wrapper for aiobotocore Athena service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_athena.client import AthenaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AthenaService(ServiceFactory[AthenaClient]):
    """
    Athena service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/)
    """
