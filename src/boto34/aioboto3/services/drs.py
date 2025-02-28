"""
Wrapper for aioboto3 Drs service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_drs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_drs.client import DrsClient

from boto34.aioboto3.service_factory import ServiceFactory


class DrsService(ServiceFactory[DrsClient]):
    """
    Drs service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_drs/)
    """
